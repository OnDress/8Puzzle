from action import Action
from state_helper import find_blank

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal_state(self, state):
        return self.goal_state == state
    
    def get_actions(self, state):
        row, col = find_blank(state)
        n = len(state) - 1
        actions = []
        if row > 0: actions.append(Action.UP)
        if row < n: actions.append(Action.DOWN)
        if col > 0: actions.append(Action.LEFT)
        if col < n: actions.append(Action.RIGHT)
        return actions

