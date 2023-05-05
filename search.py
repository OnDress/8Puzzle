from collections import deque
from heuristic import misplaced_tile
from node import Node
from node import Child
from priority_queue import Priority_Queue
from problem import Problem
from search_helper import e_state_exists
"""
def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = []
    q.append(node)
    explored = []
    while True:
        if len(q) == 0: return None
        node = q.pop(0)
        if problem.is_goal_state(node.state): return problem.solution(node,explored)
        explored.append(node.state)
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            if not e_state_exists(explored,child.state) and not q_state_exists(q,child.state):
                q.append(child)
            elif q_state_exists(q,child.state):
                i = exists_element(q,child.state)
                if q[i].cost > child.cost: 
                    child.parent = q[i].parent
                    q[i] = child"""

def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    explored = []
    while True:
        if q.is_empty(): return None
        node = q.delete_cost()
        if problem.is_goal_state(node.state): return problem.solution(node,explored)
        explored.append(node.state)
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            if not e_state_exists(explored,child.state) and not q.exists(child.state):
                q.insert(child)
            elif q.exists(child.state):
                i = q.exists_element(child.state)
                if q.at(i).cost > child.cost: 
                    q.queue[i] = child

"""
def misplaced_tile_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    explored = []
    while not q.is_empty():
        node = q.delete()
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            child.heuristic = misplaced_tile(child.state,problem.goal_state)
            child.f = child.cost + child.heuristic
            if problem.is_goal_state(node.state): return problem.solution(node,explored)
 """