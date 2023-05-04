from collections import deque
from node import Node
from problem import Problem


def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0)
    if problem.is_goal_state(node.state): return node
    q = []
    q.append(node)
    explored = set()
    while True:
        if q.empty(): return None
        node = q.pop(0)
        explored.add(node)
        for action in problem.get_actions(node.state):
            child = Node(node, action)
            if child.state not in explored and child.state not in q:
                if problem.is_goal_state(child.state): return child
                q.append(child)
