import math

def misplaced_tile(state,goal_state):
    misplaced_tile = 0
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            if state[i][j] != goal_state[i][j]: misplaced_tile += 1
    return misplaced_tile

def euclidean_distance(state):
    total_distance = 0
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            total_distance += math.dist(euclidean_helper(state[i][j]),[i,j])
    return total_distance

def euclidean_helper(num):
    if num == "1": return [0,0]
    elif num == "2": return [0,1]
    elif num == "3": return [0,2]
    elif num == "4": return [1,0]
    elif num == "5": return [1,1]
    elif num == "6": return [1,2]
    elif num == "7": return [2,0]
    elif num == "8": return [2,1]
    elif num == "0": return [2,2]

