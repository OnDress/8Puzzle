from action import Action
import copy
import node

def find_blank(state):
    blank = '0'
    for rownum, row in enumerate(state):
        for colnum,value in enumerate(row):
            if value == blank: return rownum, colnum 


def apply_action(state, action):
    new_state = copy.deepcopy(state)
    row,col = find_blank(new_state)
    if action == Action.UP: 
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
    elif action == Action.DOWN:
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
    elif action == Action.LEFT:
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
    elif action == Action.RIGHT:
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
    return new_state


