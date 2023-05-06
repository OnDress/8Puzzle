from action import Action
from node import Child
from node import Node
from state_helper import find_blank

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [["1", "2", "3"],["4", "5", "6"], ["7", "8", "0"]]
                           
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
    
    def solution(self, node, set, max_queue):
        expanded = str(len(set))
        depth = str(node.depth)
        max = str(max_queue)
        print("\nGoal Reached")
        print("To solve this problem the search algorithm expanded a total of " + expanded + " nodes.")
        print("The maximum number of nodes in the queue at any one time: " + max)
        print("The depth of the goal node was " + depth)


    def e_solution_trace(self, node, set, max_queue, initial_state):
        expanded = str(len(set))
        depth = str(node.depth)
        max = str(max_queue)
        stack = []
        print("Expanding state: ")
        for row in initial_state:
            for col in row:
                print(col, end=" ")
            print()
        print()
        while node.parent != None:
            stack.append(node)
            node = node.parent
        while len(stack) !=0:
            node = stack.pop()
            h_n = str(node.heuristic)
            g_n = str(node.cost)
            if len(stack) != 0:
                print("The best state to expand with g(n) = " + g_n + " and h(n) = " + h_n + " is: ")
            for row in node.state:
                for col in row:
                    print(col, end=" ")
                print()
            if len(stack) != 0:
                print("Expanding this node...\n")
        print()
        print("Goal Reached!")
        print("To solve this problem the search algorithm expanded a total of " + expanded + " nodes.")
        print("The maximum number of nodes in the queue at any one time: " + max)
        print("The depth of the goal node was " + depth)