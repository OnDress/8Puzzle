from collections import deque
from heuristic import misplaced_tile
from node import Node
from node import Child
from problem import Problem
from search_helper import state_exists
from search_helper import exists_element


def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0, 0)
    q = []
    q.append(node)
    explored = []
    while True:
        if len(q) == 0: return None
        node = q.pop(0)
        if problem.is_goal_state(node.state): return problem.solution(node,explored)
        explored.append(node.state)
        for action in problem.get_actions(node.state):
            child = Child(node, action, 0)
            if explored.count(child.state) == 0 and not state_exists(q,child.state):
                q.append(child)
            elif state_exists(q,child.state):
                i = exists_element(1,child.state)
                q[i] = child