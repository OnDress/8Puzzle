from collections import deque
from node import Node
from node import Child
from problem import Problem


def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0)
    explored = []#set()
    if problem.is_goal_state(node.state): return problem.solution(node,explored)
    q = []
    q.append(node)
    while True:
        if len(q) == 0: return None
        node = q.pop(0)
        explored.append(node)
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            if explored.count(child.state) == 0 and q.count(child.state) == 0:
                if problem.is_goal_state(child.state): return problem.solution(child,explored)
                q.append(child)
