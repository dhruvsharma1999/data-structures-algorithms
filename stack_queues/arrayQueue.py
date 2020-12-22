#FIFO queue implementation using a python list as underlying stoage

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10 
    def __init__(self):
        """create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elments in the queue"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Returns but do not removes the element at the front of the queue"""
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and returns the first element of the queue"""
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue"""
        if self._size == len(self._data)
      
