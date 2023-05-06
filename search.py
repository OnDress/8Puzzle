from collections import deque
from heuristic import misplaced_tile
from heuristic import euclidean_distance
from node import Node
from node import Child
from priority_queue import Priority_Queue
from problem import Problem
from search_helper import e_exists_element
from search_helper import e_state_exists

def uniform_cost_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    max_queue = 1
    explored = []
    while True:
        if len(q.queue) > max_queue: max_queue = len(q.queue)
        if q.is_empty(): return None
        node = q.delete_cost()
        if problem.is_goal_state(node.state): return problem.solution(node, explored, max_queue)
        explored.append(node.state)
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            if not e_state_exists(explored,child.state) and not q.exists(child.state):
                q.insert(child)
            elif q.exists(child.state):
                i = q.exists_element(child.state)
                if q.at(i).cost > child.cost: 
                    q.queue[i] = child

def misplaced_tile_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    max_queue = 1
    explored = []
    while not q.is_empty():
        if len(q.queue) > max_queue: max_queue = len(q.queue)
        node = q.delete_f()
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            child.heuristic = misplaced_tile(child.state,problem.goal_state)
            child.f = child.cost + child.heuristic
            if problem.is_goal_state(node.state): return problem.solution(node, explored, max_queue)
            if q.exists(child.state):
                i = q.exists_element(child.state)
                if q.at(i).cost < child.cost: break
            elif e_state_exists(explored, child.state):
                i = e_exists_element(child.state)
                if explored[i].cost < child.cost: break
            else:
                q.insert(child)
        explored.append(node)

def euclidean_distance_search(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    max_queue = 1
    explored = []
    while not q.is_empty():
        if len(q.queue) > max_queue: max_queue = len(q.queue)
        node = q.delete_f()
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            child.heuristic = euclidean_distance(child.state)
            child.f = child.cost + child.heuristic
            if problem.is_goal_state(node.state): return problem.solution(node, explored, max_queue)
            if q.exists(child.state):
                i = q.exists_element(child.state)
                if q.at(i).cost < child.cost: break
            elif e_state_exists(explored, child.state):
                i = e_exists_element(child.state)
                if explored[i].cost < child.cost: break
            else:
                q.insert(child)
        explored.append(node)

def euclidean_distance_search_trace(problem):
    node = Node(problem.initial_state, 0, 0)
    q = Priority_Queue()
    q.insert(node)
    max_queue = 1
    explored = []
    while not q.is_empty():
        if len(q.queue) > max_queue: max_queue = len(q.queue)
        node = q.delete_f()
        for action in problem.get_actions(node.state):
            child = Child(node, action)
            child.heuristic = euclidean_distance(child.state)
            child.f = child.cost + child.heuristic
            if problem.is_goal_state(node.state): return problem.e_solution_trace(node, explored, max_queue, problem.initial_state)
            if q.exists(child.state):
                i = q.exists_element(child.state)
                if q.at(i).cost < child.cost: break
            elif e_state_exists(explored, child.state):
                i = e_exists_element(child.state)
                if explored[i].cost < child.cost: break
            else:
                q.insert(child)
        explored.append(node)

 