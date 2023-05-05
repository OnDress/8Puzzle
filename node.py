from state_helper import apply_action

class Node:
    def __init__(self, state, depth, cost, heuristic):
        self.state = state
        self.depth = depth
        self.cost = cost
        self.parent = None
        self.heuristic = self.cost + heuristic
class Child:
    def __init__(self, parent, action, heuristic):
        self.parent = parent
        self.depth = parent.depth + 1
        self.cost = parent.cost + 1
        self.state = apply_action(parent.state, action)
        self.heuristic = self.cost + heuristic
        