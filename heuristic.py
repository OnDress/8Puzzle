
def misplaced_tile(state,goal_state):
    misplaced_tile = 0
    for row in state:
        for col in row:
            if state[row][col] != goal_state[row][col]: misplaced_tile += 1
    return misplaced_tile