from node import Node

class Priority_Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def insert(self, node):
        self.queue.append(node)

    def exists(self,node):
        return self.queue.count(node.state) != 0
    
    def delete(self):
        min = 999999999999
        index = 0
        for i in range(len(self.queue)):
            if self.queue[i].f < min:
                min = self.queue[i].f
                index = i
        min_f_node = self.queue[i]
        del self.queue[i]
        return min_f_node
    
