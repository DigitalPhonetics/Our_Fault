###############################################################################
#
# Copyright 2019, University of Stuttgart: Institute for Natural Language Processing (IMS)
#
# This file is part of Adviser.
# Adviser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3.
#
# Adviser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Adviser.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################

from collections import defaultdict
from typing import List, Dict

from services.service import PublishSubscribe
from services.service import Service
from utils import SysAct, SysActionType
from utils.spacejambeliefstate import BeliefState
from utils.domain.jsonlookupdomain import JSONLookupDomain
from utils.logger import DiasysLogger
from utils.useract import UserActionType
from utils.sysstate import SysState
import copy
from random import randint

class SpaceJamHandcraftedPolicy(Service):
    def __init__(self, domain: JSONLookupDomain, logger: DiasysLogger = DiasysLogger(),
                 max_turns: int = 25):
        """
        """
        super().__init__(domain=domain)
        self.domain = domain
        self.logger = logger
        # TODO: I don't think we actually need this for this case
        self.max_turns = max_turns
        self.modules = ["dials module", "button sequence module", "switches module", "button array module"]

    def dialog_start(self, user_id: str):
        self.set_state(user_id, "turn_count", 0)
        self.set_state(user_id, "last_acts", [])
        self.set_state(user_id, "current_module", 0)

    @PublishSubscribe(sub_topics=["reset"], pub_topics=["sys_acts"])
    def reset(self, user_id: str, reset):
        if reset == True:
            self.dialog_start(user_id=user_id)
            return {'sys_acts': []}

    @PublishSubscribe(sub_topics=["beliefstate"], pub_topics=["sys_acts", "sys_state"])
    def choose_sys_act(self, user_id: str = "default", beliefstate: BeliefState = None):
        current_module = self.get_state(user_id, "current_module")
        variant = [str(randint(1, 3))]
        user_act_types = beliefstate['user_acts']
        # Get and update current turn
        turn_count = self.get_state(user_id, "turn_count")
        turn_count += 1
        self.set_state(user_id, "turn_count", turn_count) 
        last_acts = self.get_state(user_id, "last_acts")

        sys_state = SysState()
        if turn_count == 1:
            # Issue greeting and describe which module to start with
            sys_acts = [SysAct(act_type=SysActionType.Welcome, slot_values={"variant": variant})]
            module = self.modules[current_module]
            sys_acts.append(SysAct(act_type=SysActionType.NextModule, slot_values={"first": ["True"], "module": [module], "variant": variant}))
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", [SysAct(act_type=SysActionType.Describe, slot_values={"module": [module], "verbose": ['True'], "variant": variant})])
            return {"sys_acts": sys_acts, "sys_state": sys_state}

        elif UserActionType.Bye in user_act_types:
            sys_acts = [SysAct(act_type=SysActionType.Bye, slot_values={"variant": variant})]
            return {"sys_acts": sys_acts}

        elif UserActionType.Repeat in user_act_types:
            sys_acts = self.get_state(user_id, "last_acts")
            return {"sys_acts": sys_acts}

        elif UserActionType.Restart in user_act_types:
            sys_acts = [SysAct(act_type=SysActionType.ConfirmRestart, slot_values={"variant": variant})]
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts, "sys_state": sys_state}
          
        elif UserActionType.RequestDescription in user_act_types:
            slot = beliefstate['request_description']["slot"]
            value = beliefstate['request_description']["value"]
            sys_acts = [SysAct(act_type=SysActionType.Describe, slot_values={slot: [value], "verbose": ['True'], "variant": variant})]
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts}

        elif beliefstate["multiple_informs"]:
            sys_acts = [SysAct(act_type=SysActionType.SlowDown, slot_values={"variant": variant})]
            return {"sys_acts": sys_acts}

        elif beliefstate["negative_inform"] and UserActionType.Inform not in user_act_types or (UserActionType.Deny in user_act_types and SysActionType.Inform in [act.type for act in last_acts]):
            # co-opting this act for the system to request where it when wrong
            if beliefstate['negative_inform'] == "general" or beliefstate['negative_inform'] is None:
                sys_acts = [SysAct(act_type=SysActionType.RequestMore, slot_values={"variant": variant})]
            elif beliefstate['negative_inform'] == "sequence":
                module = self.modules[current_module]
                color_seq = [self.get_highest_belief(beliefstate[module]['color_seq'], i) for i in range(len(beliefstate[module]["color_seq"]))]
                sys_acts = [SysAct(act_type=SysActionType.RequestMore, slot_values={"color_seq": color_seq, "variant": variant})]
            self.set_state(user_id, "last_acts", sys_acts)
            sys_state.last_acts = sys_acts
            return {"sys_acts": sys_acts, "sys_state": sys_state}

        elif UserActionType.ActionFail in user_act_types:
            # return confirm act of relevant beliefstate
            beliefs = copy.deepcopy(beliefstate[self.modules[current_module]])
            for key in beliefs:
                if key != 'ans':
                    if type(beliefs[key]) == dict:
                        belief = [self.get_highest_belief(beliefs, key)]
                        beliefs[key] = belief
                    elif type(beliefs[key]) == list:
                        belief = [self.get_highest_belief(beliefs[key], i) for i in range(len(beliefs[key]))]
                        beliefs[key] = belief
                    else:
                        beliefs[key] = [str(beliefs[key])]

            if self.modules[current_module] == "switches module" or self.modules[current_module] == "dials module":
                if self.get_highest_belief(beliefstate, 'slider') is not None:
                    beliefs["slider"] = [self.get_highest_belief(beliefstate, 'slider')]

            new_beliefs = {key: beliefs[key] for key in beliefs if key != "ans" and beliefs[key][0] != 'None'}
            new_beliefs["variant"] = variant
            sys_acts = [SysAct(act_type=SysActionType.Confirm, slot_values=new_beliefs)]
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts, "sys_state": sys_state}
        
        elif UserActionType.Forgot in user_act_types:
            sys_acts = [SysAct(act_type=SysActionType.Request, slot_values={"variant": variant, "restart": []})]
            return {"sys_acts": sys_acts}

        elif UserActionType.Deny in user_act_types and (SysActionType.NextModule in [act.type for act in last_acts] or SysActionType.Describe in [act.type for act in last_acts]):
            # return here a more thorough description
            sys_acts = [SysAct(act_type=SysActionType.Describe, slot_values={"module": [self.modules[current_module]], "verbose": ["True"], "variant": variant})]
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts, "sys_state": sys_state}
      
        elif UserActionType.ActionComplete in user_act_types and self.module_solved(beliefstate=beliefstate, module_id=current_module):
            # return a next module act
            current_module = current_module + 1 if current_module < 3 else 3
            self.set_state(user_id, "current_module", current_module)
            if current_module == 4:
                sys_acts = [SysAct(act_type=SysActionType.Bye, slot_values={"condition": ["win"], "user_id": [str(user_id)], "variant": variant})]
            else:
                sys_acts = [SysAct(act_type=SysActionType.NextModule, slot_values={"first": ['False'], "module": [self.modules[current_module]], "variant": variant})]
            sys_state.last_acts = sys_acts
            self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts, "sys_state": sys_state}

        elif SysActionType.Inform in [act.type for act in last_acts] and UserActionType.Inform not in user_act_types and UserActionType.ActionComplete not in user_act_types:
            # ask user if they completed task
            sys_acts = [SysAct(act_type=SysActionType.ConfirmAction, slot_values={"variant": variant})]
            sys_state.last_acts = sys_acts
            # self.set_state(user_id, "last_acts", sys_acts)
            return {"sys_acts": sys_acts, "sys_state": sys_state}

        elif UserActionType.Bad in user_act_types:
            sys_acts = [SysAct(act_type=SysActionType.Bad, slot_values={"variant": variant})]
            sys_state.last_acts = self.get_state(user_id, "last_acts")
            return {"sys_acts": sys_acts, "sys_state": sys_state}            

        else:
            return self.solve_module(user_id, beliefstate, module_id=current_module)

    def solve_module(self, user_id, beliefstate, module_id):
        sys_acts = None
        sys_state = SysState()

        if module_id == 0:
            sys_acts = self.solve_dials_module(beliefstate)
        elif module_id == 1:
            sys_acts = self.solve_button_sequence_module(beliefstate)
        elif module_id == 2:
            sys_acts = self.solve_switches_module(beliefstate)
        elif module_id == 3:
            sys_acts = self.solve_button_array(beliefstate)

        if sys_acts == None:
            sys_acts = [SysAct(act_type=SysActionType.Bad)]

        for act in sys_acts:
            variant = randint(1, 3)
            act.add_value(slot="variant", value=str(variant))

        if sys_acts:
            sys_state.last_acts = sys_acts
            # Add slot being asked to sys_state
            # System will only issue one request at a time, if a request is in the list, it is the only item
            if sys_acts[0].type == SysActionType.Request:
                request_slot = None
                for slot in sys_acts[0].slot_values:
                    if sys_acts[0].slot_values[slot] == []:
                        request_slot = slot
                sys_state.last_request_slot = slot
        self.set_state(user_id, "last_acts", sys_acts)
        return {"sys_acts": sys_acts, "sys_state": sys_state}

    def module_solved(self, beliefstate, module_id):
        """
            Check if current module is solved, do this by checking if answer len in the beliefstate is correct
        """
        current_module = self.modules[module_id]
        if current_module == "dials module" or current_module == "button sequence module":
            if beliefstate[current_module]["ans"]:
                return True
        elif current_module == "switches module":
            color_seq = [self.get_highest_belief(beliefstate['switches module']['color_seq'], i) for i in range(len(beliefstate['switches module']["color_seq"]))]
            if len(color_seq) == 4 and int(self.get_highest_belief(beliefstate['switches module'], "current_switch_ind")) == 4:
                return True
        elif current_module == "button array module":
            if int(self.get_highest_belief(beliefstate[current_module], 'current_round')) == 4:
                return True
        else:
            return False

    def get_highest_belief(self, bs, slot):
        if bs[slot]:
            sorted_list = sorted(bs[slot].items(), key=lambda kv: kv[1], reverse=True)
            if float(sorted_list[0][1]) > 0:
                return sorted_list[0][0]

    def solve_dials_module(self, beliefstate):
        """
            Works through instructions sequentially, asking for additional information as needed; fixed order, not really flexible
        """
        dial_beliefs = beliefstate["dials module"]
        if dial_beliefs["num_half_dials"] is None:
            sys_act = SysAct(act_type=SysActionType.Request)
            sys_act.add_value("object", "half_dial")
            sys_act.add_value("number")
            return [sys_act]
        # For now, full dials are removed from the game --LV 
        # if dial_beliefs["num_full_dials"] is None:
        #     sys_act = SysAct(act_type=SysActionType.Request)
        #     sys_act. add_value("object", "full_dial")
        #     sys_act.add_value("number")
        #     return [sys_act]
        if not beliefstate["slider"]:
            sys_act = SysAct(act_type=SysActionType.Request)
            sys_act.add_value("object", "slider")
            sys_act.add_value("color")

        # TODO: add other conditions
        num_half_dials = int(self.get_highest_belief(dial_beliefs, "num_half_dials"))
        if num_half_dials == 2:
            if self.get_highest_belief(beliefstate, "slider") == "green":
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["point_middle"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['2'], "explanation": ["green_slider"]})]

            if dial_beliefs["left_dial_number"] is None:
                sys_act = SysAct(act_type=SysActionType.Request)
                sys_act.add_value("object", "left_dial")
                sys_act.add_value("number")
                return [sys_act]
            elif int(self.get_highest_belief(dial_beliefs, "left_dial_number")) % 2 == 0:
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["largest_odd"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['2'], "explanation": ["left_dial_even"]})]

            if dial_beliefs["right_dial_pointer"] is None:
                sys_act = SysAct(SysActionType.Request)
                sys_act.add_value("object", "right_dial")
                sys_act.add_value("position")
                return [sys_act]
            elif self.get_highest_belief(dial_beliefs, "right_dial_pointer") == "right":
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["one_left_one_right"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['2'], "explanation": ["right_dial_right"]})]

            else:
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["far_left_far_right"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['2'], "explanation": ["right_dial_not_right"]})]
        elif num_half_dials == 1:
            if self.get_highest_belief(beliefstate, "slider") == "green":
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["point_left"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['1'], "explanation": ["green_slider"]})]
            
            if dial_beliefs["left_dial_number"] is None:
                return [SysAct(act_type=SysActionType.Request, slot_values={"object": ["left_dial"], "number": [], "count": ['1']})]
            elif int(self.get_highest_belief(beliefstate, "left_dial_number")) < 10:
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ['greater_ten']}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['1'], "explanation": ["less_ten"]})]
            elif int(self.get_highest_belief(beliefstate, "left_dial_number")) % 2 == 0:
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ['smallest_odd']}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['1'], "explanation": ["even"]})]
            else:
                return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["dials"], "action": ["point_right"]}),
                        SysAct(act_type=SysActionType.Explain, slot_values={"num_half_dials": ['1'], "explanation": ["default"]})]

        else:
            return [SysAct(act_type=SysActionType.Request, slot_values={"object": ["half_dial"], "number": [], "describe": []})]

    def solve_button_sequence_module(self, beliefstate):
        # TODO: Might need to revise explanations depending on the mode
        button_seq_belief = beliefstate["button sequence module"]
        if len(button_seq_belief['color_seq']) == int(self.get_highest_belief(button_seq_belief, "seq_len")):
            color_seq = [self.get_highest_belief(button_seq_belief['color_seq'], i) for i in range(len(button_seq_belief["color_seq"]))]
            if None in color_seq:
                # Should only ever be one of these at a time
                missing_pos = color_seq.index(None)
                return [SysAct(act_type=SysActionType.Request, slot_values={ "position": [str(missing_pos)], "object": ["enabled_button"], "color": []})]
           
            elif len(color_seq) == 3:
                if "amber" not in color_seq:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['0']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['3'], "explanation": ["no_amber"]})]
                elif color_seq[-1] == "blue":
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['last']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['3'], "explanation": ["last blue"]})]
                elif color_seq.count("blue") > 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['last_blue']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['3'], "explanation": ["several_blue"]})]
                else:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['0']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['3'], "explanation": ["default"]})]

            elif len(color_seq) == 4:
                if color_seq.count("green") > 1 and beliefstate["warp_drive_percent"] > 0.25:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ["last_green"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["several_green_high_warp_drive"]})]
                elif color_seq[-1] == "amber" and "blue" not in color_seq:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['0']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["last_amber_no_blue"]})]
                elif color_seq.count("green") == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['3']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["one_green"]})]
                elif color_seq.count("blue") > 1:
                    # get position of first blue button
                    pos = color_seq.index("blue")
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ["first_blue"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["several_blue"]})]
                elif color_seq.count("green") > 1 and beliefstate["warp_drive_percent"] < 0.5:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['second_last']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["several_green_low_warp_drive"]})]
                else:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['2']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['4'], "explanation": ["default"]})]
            elif len(color_seq) == 5:
                if color_seq.count("green") > 1 and beliefstate["warp_drive_percent"] > 0.25:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['0']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["several_green_high_warp_drive"]})]
                elif color_seq[-1] == "blue":
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['1']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["last_blue"]})]
                elif color_seq.count("green") == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['3']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["one_green"]})]
                elif color_seq.count("amber") == 1 and color_seq.count("green") > 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['1']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["one_amber_several_green"]})]
                elif len(set(color_seq)) == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['2']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["same_color"]})]
                else:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["enabled_button"], "position": ['last']}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"color_seq": color_seq, "num_enabled": ['5'], "explanation": ["default"]})]
        elif int(self.get_highest_belief(button_seq_belief, "seq_len")) > 5:
            return [SysAct(act_type=SysActionType.Request, slot_values={"object": ["enabled_button"], "number": [], "describe": []})]
        else:
            next_pos = len(button_seq_belief['color_seq'])
            if beliefstate['inform_grey']:
                return [SysAct(act_type=SysActionType.Request, slot_values={ "position": [str(next_pos)], "object": ["enabled_button"], "color": [], "not_grey": []})]
            else:
                return [SysAct(act_type=SysActionType.Request, slot_values={ "position": [str(next_pos)], "object": ["enabled_button"], "color": []})]


    def solve_switches_module(self, beliefstate):
        current_switch_ind = int(self.get_highest_belief(beliefstate["switches module"],"current_switch_ind"))
        color_seq = [self.get_highest_belief(beliefstate['switches module']['color_seq'], i) for i in range(len(beliefstate['switches module']["color_seq"]))]
        # if the switches
        include_slider = False
        if len(color_seq) <= current_switch_ind + 1 and current_switch_ind < 3:
            return [SysAct(act_type=SysActionType.Request, slot_values={"color": [], "object": ["switch"], "position": [str(len(color_seq))]})]

        elif None in color_seq:
            missing_pos = color_seq.index(None)
            return [SysAct(act_type=SysActionType.Request, slot_values={"color": [], "object": ["switch"], "position": [str(missing_pos)]})]
            
        else:
            direction = None
            explanation = None
            if color_seq[current_switch_ind] == "blue":
                if color_seq[:current_switch_ind].count("blue") == 0:
                    if current_switch_ind < 3 and color_seq[current_switch_ind + 1] == "green":
                        direction = "right"
                        explanation = "first_blue_next_green"
                    else:
                        direction = "left"
                        explanation = "first_blue"
                elif color_seq[:current_switch_ind].count("blue") == 1:
                    if color_seq[current_switch_ind - 1] == "amber" or color_seq[current_switch_ind - 1] == "blue":
                        direction = "right"
                        explanation = "second_blue_after_amber_or_blue"
                    else:
                        direction = "left"
                        explanation = "second_blue"
                elif color_seq[:current_switch_ind].count("blue") == 2:
                    if color_seq.count("green") >= 1:
                        direction = "right"
                        explanation = "third_blue_a_green"
                    else:
                        direction = "left"
                        explanation = "third_blue"


                elif color_seq[:current_switch_ind].count("blue") == 3:
                    # Neither side should be active
                    explanation = "fourth_blue"
                    pass

            elif color_seq[current_switch_ind] == "green":
                if color_seq[:current_switch_ind].count("green") == 0:
                    if color_seq.count("amber") >= 1 and self.get_highest_belief(beliefstate, "slider") == "green":
                        direction = "right"
                        include_slider = True
                        explanation = "first_green_a_amber_green_slider"
                    else:
                        direction = "left"
                        include_slider = True
                        explanation = "first_green"
                elif color_seq[:current_switch_ind].count("green") == 1:
                    if color_seq[current_switch_ind - 1] == "green":
                        direction = "right"
                        explanation = "second_green_after_green"
                    else:
                        direction = "left"
                        explanation = "second_green"
                elif color_seq[:current_switch_ind].count("green") == 2:
                    # Neither side should be active
                    pass
                elif color_seq[:current_switch_ind].count("green") == 3:
                    if self.get_highest_belief(beliefstate, "slider") == "red":
                        direction = "right"
                        include_slider = True
                        explanation = "fourth_green_red_slider"
                    else:
                        direction = "left"
                        explanation = "fourth_green"

            elif color_seq[current_switch_ind] == "amber":
                if color_seq[:current_switch_ind].count("amber") == 0:
                    if current_switch_ind < 3 and color_seq[current_switch_ind + 1] == "green":
                        direction = "right"
                        explanation = "first_amber_next_green"
                    else:
                        direction = "left"
                        explanation = "first_amber"
                elif color_seq[:current_switch_ind].count("amber") == 1:
                    if color_seq[current_switch_ind - 1] == "amber" or color_seq[current_switch_ind - 1] == "blue":
                        direction = "right"
                        explanation = "second_amber_after_amber_or_blue"
                    else:
                        direction = "left"
                        explanation = "second_amber"
                elif color_seq[:current_switch_ind].count("amber") == 2:
                    if color_seq.count("green") >= 1:
                        direction = "right"
                        explanation = "third_amber_a_green"
                    else:
                        direction = "left"
                        explanation = "third_amber"
                elif color_seq[:current_switch_ind].count("amber") == 3:
                    # Neither side should be active
                    pass

            evidence = {"color_seq": color_seq, "position": [str(current_switch_ind)], "explanation": [explanation]}
            if include_slider:
                evidence["slider"] = [self.get_highest_belief(beliefstate, "slider")]

            return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["switch"], "position": [str(current_switch_ind)], "action": [direction]}),
                    SysAct(act_type=SysActionType.Explain, slot_values=evidence)]



    def solve_button_array(self, beliefstate):
        current_round = int(self.get_highest_belief(beliefstate["button array module"], "current_round"))
        active_column = self.get_highest_belief(beliefstate["button array module"], "active_column")
        if active_column is None or int(active_column) == -1:
            return [SysAct(act_type=SysActionType.Request, slot_values={"position": [], "object": ["column"]})]
        else:
            active_column = int(active_column)
            if current_round == 0:
                if active_column == 0:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "position": ['1'], "action": ["first_button_same_color"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "position": ['0'], "action": ["second_button"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 2:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "position": ['1'], "action": ["first_button_same_color"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]

            if current_round == 1:
                if active_column == 0:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "position": ['2'], "action": ["last_button_same_color"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_1"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 2:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_1"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]

            if current_round == 2:
                if active_column == 0:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["color_round_2"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_1"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 2:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "position": ['0'], "action": ["last_button_same_color"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]

            if current_round == 3:
                if active_column == 0:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_2"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 1:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_1"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]
                elif active_column == 2:
                    return [SysAct(act_type=SysActionType.Inform, slot_values={"object": ["column"], "action": ["button_round_3"]}),
                            SysAct(act_type=SysActionType.Explain, slot_values={"current_round": [str(current_round)], "active_column": [str(active_column)]})]