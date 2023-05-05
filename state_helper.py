from action import Action
import copy

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

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()