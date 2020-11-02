#implementing queue in python using lists

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    #adding item at the end of the queue
    def enqueue(self, item):
        self.items.insert(0, item)
    
    #removing elements from the front of the queue
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
