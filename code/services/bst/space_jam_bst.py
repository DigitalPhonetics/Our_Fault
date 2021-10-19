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

from typing import List, Set, Dict, Any

from services.service import PublishSubscribe
from services.service import Service
from utils.spacejambeliefstate import BeliefState
from utils.useract import UserActionType, UserAct
from utils.sysstate import SysState
from utils.sysact import SysActionType


class SpaceJamBST(Service):
    """
    A rule-based approach on belief state tracking.
    The state is basically a dictionary of keys.
    """
    BELIEFSTATE = "beliefstate"

    def __init__(self, domain=None, logger=None):
        Service.__init__(self, domain=domain)
        self.logger = logger
        self.sys_state = {}

    @PublishSubscribe(sub_topics=["sys_state"])
    def update_sys_state(self, user_id: str = "default", sys_state={}):
        self.set_state(user_id, "sys_state", sys_state)

    @PublishSubscribe(sub_topics=["user_acts"], pub_topics=["beliefstate"])
    def update_bst(self, user_id: str = "default", user_acts: List[UserAct] = None) \
            -> dict(beliefstate=BeliefState):
        """
            Function for updating the current dialog belief state (which tracks the system's
            knowledge about what has been said in the dialog) based on the user actions generated
            from the user's utterances

            Args:
                belief_state (BeliefState): this should be None
                user_acts (list): a list of UserAct objects mapped from the user's last utterance
                sys_state (SysState): last system action

            Returns:
                (dict): a dictionary with the key "beliefstate" and the value the updated
                        BeliefState object

        """
        # save last turn to memory
        bs = self.get_state(user_id, SpaceJamBST.BELIEFSTATE)
        sys_state = self.get_state(user_id, "sys_state")
        bs.start_new_turn()
        if user_acts:
            # self._reset_informs(bs, user_acts)
            self._reset_requests(bs)
            bs['multiple_informs'] = False
            bs["inform_grey"] = False
            bs["negative_inform"] = None
            bs["user_acts"] = self._get_all_usr_action_types(bs, user_acts)

            self._handle_user_acts(bs, user_acts, sys_state)

            # num_entries, discriminable = bs.get_num_dbmatches()
            # bs["num_matches"] = num_entries
            # bs["discriminable"] = discriminable

        self.set_state(user_id, SpaceJamBST.BELIEFSTATE, bs)
        return {'beliefstate': bs}

    @PublishSubscribe(sub_topics=["reset"])
    def reset(self, user_id: str, reset):
        if reset == True:
            self.dialog_start(user_id=user_id)

    def dialog_start(self, user_id: str):
        """
            Resets the belief state so it is ready for a new dialog

            Returns:
                (dict): a dictionary with a single entry where the key is 'beliefstate'and
                        the value is a new BeliefState object
        """
        # initialize belief state
        self.set_state(user_id, SpaceJamBST.BELIEFSTATE, BeliefState(self.domain))
        self.set_state(user_id, "sys_state", {})

    # def _reset_informs(self, bs: BeliefState, acts: List[UserAct]):
    #     """
    #         If the user specifies a new value for a given slot, delete the old
    #         entry from the beliefstate
    #     """
    #
    #     slots = {act.slot for act in acts if act.type == UserActionType.Inform}
    #     for slot in [s for s in bs['informs']]:
    #         if slot in slots:
    #             del bs['informs'][slot]

    def _reset_requests(self, bs: BeliefState):
        """
            gets rid of requests from the previous turn
        """
        bs['requests'] = {}
        bs['request_description'] = {}

    def _get_all_usr_action_types(self, bs: BeliefState, user_acts: List[UserAct]) -> Set[UserActionType]:
        """ Returns a set of all different user action types in user_acts.

        Args:
            user_acts: list of UsrAct objects

        Returns:
            set of UserActionType objects
        """
        action_type_set = set()
        for act in user_acts:
            action_type_set.add(act.type)
        return action_type_set

    def _handle_user_acts(self, bs: BeliefState, user_acts: List[UserAct], sys_state: SysState):

        """
            Updates the belief state based on the information contained in the user act(s)

            Args:
                beliefstate (BeliefState): the belief state to be updated
                user_act (list[UserAct]): the list of user acts to use to update the belief state

        """
        # TODO: should requests have a score at all? For now I'm leaving that out, but might be
        #  worth revisiting later

        current_module = bs['current_module']
        if sys_state:
            # Iterate through acts and make sure nothing needs to be adjusted based on sys_state
            for act in sys_state.last_acts:
                if act.type == SysActionType.NextModule:
                    current_module = act.slot_values['module'][0]
                    bs['current_module'] = current_module
                    bs['slider'] = {"green": 1.0}
                elif act.type == SysActionType.Inform:
                    bs[current_module]['ans'].append(act.slot_values)

        context = {}
        for act in user_acts:
            if act.type == UserActionType.Inform:
                if act.slot in context:
                    bs["multiple_informs"] = True
                if act.slot == "object":
                    context["object"] = act.value
                if act.slot == "position":
                    if act.value == "last":
                        context["position"] = act.value
                    else:
                        context["position"] = int(act.value)
                if act.slot == "color":
                    context["color"] = act.value
        # Handle user acts
        for act in user_acts:
            if act.type == UserActionType.RequestDescription:
                bs['request_description']["slot"] = act.slot
                bs['request_description']["value"] = act.value
            elif act.type == UserActionType.RequestExplanation:
                bs['requests_explanation'][act.slot] = act.score
            elif act.type == UserActionType.Inform:
               bs = self._decode_inform(bs, act.slot, act.value, act.score, current_module,
                                        sys_state, context)
            elif act.type == UserActionType.NegativeInform:
                # reset mentioned value to zero probability
                self._decode_negative_inform(bs, act.slot, act.value, current_module, sys_state, context)
            elif act.type == UserActionType.ActionComplete:
                if current_module == 'button array module':
                    current_round = self.get_highest_belief(bs[current_module], "current_round")
                    bs[current_module]['current_round'] = {current_round + 1: 1.0}
                    bs[current_module]['active_column'] = None
                elif current_module == 'switches module':
                    current_switch = self.get_highest_belief(bs[current_module], "current_switch_ind")
                    bs[current_module]["current_switch_ind"] = {current_switch + 1: 1.0}
            elif act.type == UserActionType.ActionFail:
                # In case of a failing action, the module is reset to the beginning. The last answer
                # of the system is removed from the answer list, and the slider is set to a random
                # position the system does not know
                # bs.reset_module(current_module)
                if current_module == "switches module":
                    bs[current_module]['current_switch_ind'] = {0: 1.0}
                elif current_module == "button array module":
                    bs[current_module]['current_round'] = {0: 1.0}
                    bs[current_module]['active_column'] = None
                if bs[current_module]['ans']:
                    bs[current_module]['ans'].pop()
                # bs['slider'] = {"green": 1.0}
            elif act.type == UserActionType.Confirm and SysActionType.ConfirmRestart in [act.type for act in sys_state.last_acts]:
                bs['slider'] = {"green": 1.0}
                if current_module == "switches module":
                    bs[current_module] = {"current_switch_ind": {0: 1.0},
                                          "color_seq": [],
                                          "ans": []
                                         }
                elif current_module == "dials module":
                    bs[current_module] = {"num_half_dials": None,
                                          "num_full_dials": None,
                                          "left_dial_pointer": None,
                                          "right_dial_pointer": None,
                                          "left_dial_number": None,
                                          "right_dial_number": None,
                                          "ans": []
                                         }
                elif current_module == "button sequence module":
                    bs[current_module] = {"color_seq": [],
                                          "seq_len": {3: 1.0},
                                          "ans": []                        
                                         }
                elif current_module == "button array module":
                    bs[current_module] = {"active_column": None,
                                          "current_round": {0: 1.0},
                                          "ans": []
                                         }

    def _decode_negative_inform(self, bs: BeliefState, slot: str, value: Any,
                                current_module: str, sys_state: SysState, context={}):
        current_module = bs["current_module"]
        if "object" in context:
            if context["object"] == "slider":
                bs["slider"] = {value: 0.0}
            elif current_module == "button sequence module" and "position" in context:
                position = len(bs['button sequence module']["color_seq"]) -1 if context["position"] == "last" else int(context["position"])
                bs["button sequence module"]["color_seq"][position][value] = 0.0
            elif current_module == "switches module" and "position" in context:
                position = 3 if context["position"] == "last" else int(context["position"])
                bs["switches module"]["color_seq"][position][value] = 0.0
            else:
                bs["negative_inform"] = 'general'
        else:
            bs["general_negative_inform"] = 'general'

    def _decode_inform(self, bs: BeliefState, slot: str, value: Any, score: float,
                       current_module: str, sys_state: SysState, context={}):
        # use amber synonyms in all modules except for the slider (because the slider
        # distinguishes between amber, orange and yellow
        amber_synonyms = {'orange', 'yellow'}

        last_sys_request = {}
        for act in sys_state.last_acts:
            if act.type == SysActionType.Request:
                last_sys_request = act.slot_values.copy()

        # TODO: assume for now that there can only be one value per slot
        _object = context["object"] if "object" in context else last_sys_request.get('object', None)
        _object = _object[0] if type(_object) == list else _object
        module_bs = bs[current_module]

        if _object == 'slider':
            # What is the color of the slider?
            if slot == 'color':
                bs['slider'] = self._set_value(bs['slider'], value, score)
        if _object == 'warp_drive_percent' and slot == 'number':
            number = float(value) / 100
            bs['warp_drive_percent'] = self._set_value(bs['warp_drive_percent'], number, score)
        if current_module == 'dials module':
            # How many full dials / half dials are in the module?
            if slot == 'number':
                if _object == "half_dial":
                    module_bs['num_half_dials'] = self._set_value(module_bs['num_half_dials'],
                                                                  int(value), score)
                elif _object == "full_dial":
                    module_bs['num_full_dials'] = self._set_value(module_bs['num_full_dials'],
                                                                  int(value), score)
                elif _object == "left_dial":
                    module_bs['left_dial_number'] = self._set_value(module_bs['left_dial_number'],
                                                                    int(value), score)
                elif _object == "right_dial":
                    module_bs['right_dial_number'] = self._set_value(module_bs['right_dial_number'],
                                                                     int(value), score)
            elif slot == 'direction':
                if _object == "left_dial":
                    module_bs['left_dial_pointer'] = self._set_value(module_bs['left_dial_pointer'],
                                                                     value, score)
                elif _object == "right_dial":
                    module_bs['right_dial_pointer'] = self._set_value(module_bs['right_dial_pointer'],
                                                                      value, score)


        elif current_module == 'button sequence module':
            # How many enabled buttons are in the sequence?
            if "color" in last_sys_request and slot == "number":
                val = value if (type(value) == int or type(value) == str) else value[0]
                if int(val) == 0 and len(module_bs['color_seq']) >= 3:
                    module_bs['seq_len'] = {len(module_bs['color_seq']): 1.0}
            elif slot == 'number':
                if value == 'one more':
                    value = len(module_bs["color_seq"]) + 1
                if int(value) == 0:
                    bs["negative_inform"] = "sequence"
                if int(value) >= len(module_bs["color_seq"]) and int(value) > 3:
                    module_bs['seq_len'] = {int(value): 1.0}
                elif int(value) > 3:
                    module_bs['seq_len'] = {int(value): 1.0}
                    module_bs['color_seq'] = module_bs["color_seq"][:int(value)]
            # What is the color of the n-th button?
            elif ('position' in last_sys_request or 'position' in context) and _object == 'enabled_button' and slot == 'color':
                value = 'amber' if value in amber_synonyms else value
                position = context["position"] if "position" in context else int(last_sys_request['position'][0])
                position = len(module_bs['color_seq']) - 1 if position == "last" else position
                if value == "grey":
                    bs["inform_grey"] = True                    
                elif position == len(module_bs['color_seq']):
                    module_bs['color_seq'].append({value: score})
                elif position < len(module_bs['color_seq']):
                    module_bs['color_seq'][position] = self._set_value(module_bs['color_seq'][position],
                                                                       value, score)
                else:
                    # TODO: Figure out how to actually handle this case
                    module_bs['seq_len'] = {position: 1.0}

        elif current_module == 'switches module':
            # What is the color of the n-th switch?
            if _object == 'slider':
                # What is the color of the slider?
                if slot == 'color':
                    bs['slider'] = self._set_value(bs['slider'], value, score)
            elif _object == "switch" and ('position' in context or "position" in last_sys_request) and slot == 'color':
                value = 'amber' if value in amber_synonyms else value
                position = context['position'] if 'position' in context else int(last_sys_request['position'][0])
                position = len((module_bs['color_seq'])) - 1 if position == "last" else position

                if position == len(module_bs['color_seq']):
                    module_bs['color_seq'].append({value: score})
                elif position < len(module_bs["color_seq"]):
                    module_bs['color_seq'][position] = {value: score}
                else:
                    # TODO: figure out how to make sure this can't happen
                    print("PROBLEM")
            elif slot == "number":
                bs['negative_inform'] = "sequence"

        elif current_module == 'button array module':
            if slot == 'position':
                value = 2 if value == "last" else value
                module_bs['active_column'] = self._set_value(module_bs['active_column'],
                                                             int(value), score)
            elif slot == 'number' and int(value) <= 3:
                value = int(value) - 1
                module_bs['active_column'] = self._set_value(module_bs['active_column'],
                                                             int(value), score)                
        return bs

    def _set_value(self, bs_values: Dict[Any, float], value: Any, score: float = 1.0):
        if bs_values is None:
            return {value: score}
        bs_values = {key: 0.0 for key in bs_values.keys()}
        bs_values[value] = score
        return bs_values

    def get_highest_belief(self, bs, slot):
        return sorted(bs[slot].items(), key=lambda kv: kv[1], reverse=True)[0][0]
