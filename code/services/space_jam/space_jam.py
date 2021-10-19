from services.service import PublishSubscribe
from services.service import Service
from utils.logger import DiasysLogger
import random

class Game(Service):
    def __init__(self, domain='space_jam', logger: DiasysLogger = DiasysLogger()):
        Service.__init__(self, domain=domain, debug_logger=logger)

    def is_dial_module_complete(self, game_state):
        """
            Based on the current game state, evaluates if the module has been correctly
            completed or not.

            Args:
                game_state (GameState): GameState object describing original and current configuration of the board
            
            Return:
                (bool): True if module has been correctly completed, False if module has been incorrectly completed
                        None if module has not yet been completed
        """
        half_dials = 0
        full_dials = 0
        dials = game_state.dials
        for d in dials:
            # can't evaluate if module is correct, until all dials have been repositioned
            if d.current_position == d.start_position:
                return
            if d.shape == "half":
                half_dials +=1
            elif d.shape == "full":
                full_dials += 1

        # Check if the current positions are correct
        if half_dials == 1 and full_dials == 0:
            """TODO: add more rules later"""

        elif half_dials == 2 and full_dials == 0:
            if game_state.slider == "green":
                if dials[0].current_position == 2 and dials[1].current_position == 2:
                    return True
            elif dials[0].start_position % 2 == 0:
                labels_2 = dials[1].labels
                expected_pos = 0
                largest_odd = 1
                for i, label in enumerate(labels_2):
                    if label % 2 == 1 and label > largest_odd:
                        largest_odd = label
                        expected_pos = i
                if dials[0].current_position == expected_pos and dials[1].current_position == expected_pos:
                    return True
            elif dials[1].start_position == 4:
                if dials[1].current_position == 3 and dials[0].current_position == dials[0].start_position + 1:
                    return True
            else:
                if dials[0].current_position == 0 and dials[1].current_position == 4:
                    return True

        return False
                    

    def is_toggle_switch_module_complete(self, game_state):
        """
            Based on the current game state, evaluates if the module has been correctly
            completed or not.

            Args:
                game_state (GameState): GameState object describing original and current configuration of the board
            
            Return:
                (bool): True if module has been correctly completed, False if module has been incorrectly completed
                        None if module has not yet been completed
        """

        # TODO: Some cases (which have been left out for now) would require a toggle not to be pushed; fix to allow that in future
        # Checks that all of the switches have actually been activeated
        for i, toggle in enumerate([switch for switch in game_state.toggle_switches if switch.active_side is not None]):

            # Handle all blue switches
            if toggle.color == "blue":
                count = [t.color for t in game_state.toggle_switches[:i]].count("blue")
                if count == 0:
                    if game_state.toggle_switches[i+1].color == "green":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != 'left':
                            return False
                elif count == 1:
                    if game_state.toggle_switches[i-1].color == "amber" or game_state.toggle_switches[i-1].color == "green":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                elif count == 2:
                    if "green" in [t.color for t in game_state.toggle_switches]:
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                elif count == 3:
                    if toggle.active_side is not None:
                        return False

            # Handle all green switches
            elif toggle.color == "green":
                count = [t.color for t in game_state.toggle_switches[:i]].count("green")
                if count == 0:
                    if "amber" in [t.color for t in game_state.toggle_switches] and game_state.slider == "green":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                if count == 1:
                    if game_state.toggle_switches[i-1].color == "green":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                if count == 2:
                    if toggle.active_side is not None:
                        return False
                if count == 3:
                    if game_state.slider == "red":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            errrors = True

            # Handle all amber switches
            elif toggle.color == "amber":
                count = [t.color for t in game_state.toggle_switches[:i]].count("amber")
                if count == 0:
                    if game_state.toggle_switches[i+1].color == "green":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                elif count == 1:
                    if game_state.toggle_switches[i-1].color == "amber" or game_state.toggle_switches[i-1].color == "blue":
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                elif count == 2:
                    if "green" in [t.color for t in game_state.toggle_switches]:
                        if toggle.active_side != "right":
                            return False
                    else:
                        if toggle.active_side != "left":
                            return False
                elif count == 3:
                    if toggle.active_side is not None:
                        return False
            if i == 3:
                return True

    def is_button_sequence_module_complete(self, games_state):
        """
            Based on the current game state, evaluates if the module has been correctly
            completed or not.

            Args:
                game_state (GameState): GameState object describing original and current configuration of the board
            
            Return:
                (bool): True if module has been correctly completed, False if module has been incorrectly completed
                        None if module has not yet been completed
        """

        enabled_buttons = [button for button in games_state.button_sequence if button.color != "disabled"]
        active_index = None
        warp_percent = games_state.complete_modules / games_state.num_modules
        button_colors = [button.color for button in enabled_buttons]
        for i in range(len(enabled_buttons)):
            if enabled_buttons[i].active == True:
                active_index = i
                break
        
        # Handle case with 3 enabled buttons
        if len(enabled_buttons) == 3:
            if "amber" not in button_colors:
                if active_index == 0:
                    return True
            elif enabled_buttons[-1].color == "amber":
                if active_index == len(enabled_buttons) -1:
                    return True
            elif button_colors.count("blue") > 1:
                if enabled_buttons[active_index].color == "blue" and button_colors[active_index + 1:].count("blue") == 0:
                    return True
            else:
                if active_index == 1:
                    return True
                else:
                    return False

        # Handle case with 4 enabled buttons
        elif len(enabled_buttons) == 4:
            if button_colors.count("green") > 1 and warp_percent > 0.25:
                if enabled_buttons[active_index].color == "green" and button_colors[active_index + 1:].count("green") == 0:
                    return True
            elif enabled_buttons[-1].color == "amber" and button_colors.count("blue") == 0:
                if active_index == 0:
                    return True
            elif button_colors.count("green") == 1:
                if active_index == 3:
                    return True
            elif button_colors.count("blue") > 1:
                if enabled_buttons[active_index].color == "blue" and button_colors[:active_index].count("blue") == 0:
                    return True
            elif button_colors.count("green") > 1 and warp_percent < 0.5:
                if active_index == len(enabled_buttons) - 2:
                    return True
            else:
                if active_index == 2:
                    return True
                else:
                    return False

        # Handle case with all 5 buttons active
        elif len(enabled_buttons) == 5:
            if button_colors.count("green") > 1 and warp_percent > 0.25:
                if active_index == 0:
                    return True
            elif enabled_buttons[-1].color == "blue":
                if active_index == 1:
                    return True
            elif button_colors.count("green") == 1:
                if active_index == 3:
                    return True
            elif button_colors.count("amber") == 1 and button_colors.count("green") > 1:
                if active_index == 1:
                    return True
            elif len(set(button_colors)) == 1:
                if active_index == 2:
                    return True
            else:
                if active_index == len(enabled_buttons) -1:
                    return True
                else:
                    return False

    def is_memory_module_complete(self, game_state):
        """
            Based on the current game state, evaluates if the module has been correctly
            completed or not.

            Args:
                game_state (GameState): GameState object describing original and current configuration of the board
            
            Return:
                (bool): True if module has been correctly completed, False if module has been incorrectly completed
                        None if module has not yet been completed
        """
        level = game_state.memory_stage
        array = game_state.memory_array
        if level == 0:
            level_info = game_state.memory_stages
            sys_button = level_info[level]['sys_button']
            user_button = level_info[level]['user_button']
            if sys_button[0] == 0 or sys_button[0] == 2:
                # check for first button of same color in second row
                if not (user_button[0] == 1 and array[sys_button[0]][sys_button[1]].color == array[user_button[0]][user_button[1]].color\
                        and array[1][:user_button[1]].count(array[user_button[0]][user_button[1]].color) == 0):
                    return False
            elif sys_button[0] == 1:
                # check for second button in first row
                if not(user_button == (1, 0)):
                    return False
        elif level == 1:
            level_info = game_state.memory_stages
            sys_button = level_info[level]['sys_button']
            user_button = level_info[level]['user_button']
            if sys_button[0] == 0:
                # Check for last button of same color in third column
                if not (user_button[0] == 2 and array[sys_button[0]][sys_button[1]].color == array[user_button[0]][user_button[1]].color\
                        and array[2][user_button[1] + 1:].count(array[user_button[0]][user_button[1]].color) == 0):
                    return False
            elif sys_button[0] == 1 or sys_button[0] == 2:
                if not (user_button == game_state.memory_stages[0]['user_button']):
                    return False
        elif level == 2:
            level_info = game_state.memory_stages
            sys_button = level_info[level]['sys_button']
            user_button = level_info[level]['user_button']
            u_button_1 = game_state.memory_stages[1]["user_button"]
            u_button_0 = game_state.memory_stages[0]["user_button"]
            if sys_button[0] == 0:
                # check in column 2, same color as button from round 2
                if not (user_button[0] == 1 and array[user_button[0]][user_button[1]].color == array[u_button_1[0]][u_button_1[1]].color):
                    return False
            if sys_button[0] == 1:
                # check that button is same as from round 1
                if not (user_button == u_button_0):
                    return False
            elif sys_button[0] == 2:
                # Check for last button of same color in first column
                if not (user_button[0] == 0 and array[sys_button[0]][sys_button[1]].color == array[user_button[0]][user_button[1]].color\
                        and array[2][user_button[1] + 1:].count(array[user_button[0]][user_button[1]].color) == 1):
                    return False
        elif level == 3:
            level_info = game_state.memory_stages
            sys_button = level_info[level]['sys_button']
            user_button = level_info[level]['user_button']
            u_button_1 = game_state.memory_stages[1]["user_button"]
            u_button_0 = game_state.memory_stages[0]["user_button"]
            u_button_2 = game_state.memory_stages[2]['user_button']
            if sys_button[0] == 0:
                # check same button as round 2
                if user_button == u_button_1:
                    return True
                else:
                    return False
            if sys_button[0] == 1:
                if user_button == u_button_0:
                    return True
                else:
                    return False
            if sys_button[0] == 2:
                if user_button == u_button_2:
                    return True
                else:
                    return False


class GameState():
    def __init__(self):
        """
            Object that describes the setup of the game board, for now supports only a fixed setup
            but if we add more levels in the future, this could be instantiated from a description file
        """
        self.reset()
        self.num_modules = 4
        self.complete_modules = 0

    def reset(self):
        self.button_sequence = [Button("amber"), Button("blue"), Button("disabled"), Button("amber"), Button("blue")]
        self.slider = "yellow"
        self.possible_slider_pos = ["green", "yellow", "amber", "orange", "red"]
        self.dials = [Dial("half", 1, [1, 15, 27, 3, 18]), Dial("half", 4, [2, 13, 32, 25, 19])]
        self.toggle_switches = [Toggle("blue"), Toggle("green"), Toggle("amber"), Toggle("blue")]
        self.memory_array = [[Button("amber"), Button("amber"), Button("green"), Button("blue")],
                       [Button("green"), Button("blue"), Button("green"), Button("amber")],
                       [Button("amber"), Button("green"), Button("blue"), Button("blue")]]
        self.memory_stages = [{"sys_button": (2, 0), "user_button": None},
                              {"sys_button": (0, 2), "user_button": None},
                              {"sys_button": (1, 1), "user_button": None},
                              {"sys_button": (0, 3), "user_btutton": None}]
        self.memory_stage = 0
        self.complete_modules = 0

    def reset_dials(self):
        for dial in self.dials:
            dial.current_position = dial.start_position

    def reset_button_sequence(self):
        for button in self.button_sequence:
            button.active = False

    def reset_toggle_switches(self):
        for toggle in self.toggle_switches:
            toggle.active_side = None  

    def reset_memory(self):
        for col in range(len(self.memory_array)):
            for row in range(len(self.memory_array[col])):
                self.memory_array[col][row].active = False
        self.memory_stages = [{"sys_button": (2, 0), "user_button": None},
                              {"sys_button": (0, 2), "user_button": None},
                              {"sys_button": (1, 1), "user_button": None},
                              {"sys_button": (0, 3), "user_btutton": None}]
        self.memory_stage = 0

    def update_button_sequence(self, button_id):
        button_id = int(button_id.split("_")[2])
        for button in self.button_sequence:
            button.active = False
        self.button_sequence[button_id].active = True

    def update_dials(self, dial_id, dial_position):
        dial_id = int(dial_id[5])
        self.dials[dial_id].current_position = int(dial_position)

    def update_toggle_switches(self, toggle_id, toggle_active):
        toggle_info = toggle_id.split("_")
        toggle_id = toggle_info[2]
        active_side = toggle_info[0]
        self.toggle_switches[int(toggle_id)].active_side = active_side if toggle_active else None

    def update_memory(self, button_id, button_active):
        col = int(button_id.split("_")[1])
        row = int(button_id.split("_")[2])
        if button_active:
            for x in range(len(self.memory_array)):
                for y in range(len(self.memory_array[x])):
                    self.memory_array[x][y].active = False
        self.memory_array[col][row].active = button_active
        self.memory_stages[self.memory_stage]['user_button'] = (col, row)

    def next_memory_stage(self):
        self.memory_stage += 1

    def add_complete_modules(self):
        self.complete_modules += 1

    def new_slider_pos(self):
        # self.slider = random.choice(self.possible_slider_pos)
        # For the expirent, let's leave this fixed
        color_seq = ["yellow", "green", "orange", "amber", "red"]
        self.slider = color_seq[self.complete_modules]
        return self.slider
        


class Button():
    def __init__(self, color):
        self.active = False
        self.color = color

    def __repr__(self):
        return f"(Color: {self.color}, Active: {self.active})\n"

class Toggle():
    def __init__(self, color):
        self.color = color
        self.active_side = None

    def __repr__(self):
        return f"(Color: {self.color}, Active Side: {self.active_side})\n"


class Dial():
    def __init__(self, shape, start_position, labels):
        self.shape = shape
        self.start_position = start_position
        self.current_position = start_position
        self.labels = labels
