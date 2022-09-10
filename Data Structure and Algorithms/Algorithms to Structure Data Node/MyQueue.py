from Node import Node
class MyQueue:
    def __init__(self):
        self.queue = []
    def add(self,new_node):
        self.queue.insert(0,new_node)


    def remove(self):
        if len(self.queue) >= 0:
            return self.queue.pop()
        return None

    def peek(self):        
        if len(self.queue) <= 0:
            return None
        return self.queue[len(self.queue) -1]



