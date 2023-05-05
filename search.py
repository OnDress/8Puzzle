from collections import deque
from node import Node
from node import Child
from problem import Problem


def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0, 0)
    q = []
    q.append(node)
    explored = []
    while True:
        if len(q) == 0: return None
        node = q.pop(0)
        if problem.is_goal_state(node.state): return problem.solution(node,explored)
        explored.append(node)
        for action in problem.get_actions(node.state):
            child = Child(node, action, 0)
            if explored.count(child.state) == 0 and q.count(child.state) == 0:
                q.append(child)
            elif q.count(child.state) != 0: 
                 i = q.index(child.state)
                 if q[i].cost > child.cost: q[i] = child

