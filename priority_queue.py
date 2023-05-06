from node import Node

class Priority_Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def insert(self, node):
        self.queue.append(node)

    def exists(self,state):
        i = 0
        while i < len(self.queue):
            if self.queue[i].state == state: return True
            i += 1
        return False
    
    def at(self,index):
        return self.queue[index]

    def exists_element(self,state):
        i = 0
        while i < len(self.queue):
            if self.queue[i].state == state: return i
            i += 1
        return False
    
    def delete_cost(self):
        min = float("inf")
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i].cost < min:
                min = self.queue[i].cost
                index = i
        min_cost_node = self.queue[index]
        del self.queue[index]
        return min_cost_node
    
    def delete_f(self):
        min = float("inf")
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i].f < min:
                min = self.queue[i].f
                index = i
        min_f_node = self.queue[index]
        del self.queue[index]
        return min_f_node
    
