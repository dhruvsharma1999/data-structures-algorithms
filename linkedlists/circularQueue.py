class CircularQueue:
    """queue implementation using circularly  linked list for storage """

    class Empty(Exception):
        """Error attempting to access an element from an empty container"""
    pass
  
    class Node:
        """Lightweight, non public class for storing a singly linked node"""
        __slots__ = '_element_', '_next' 

        def __init__(self, element, next):
            self._element = element
            self._next = next 

    def __init__(self):
        """create an empty queue"""
        self._tail = None 
        self._size = 0

    def __len__(self):
        """Returns number of element in the list"""
        return self._size 

    def is_empty(self):
        """Returns ture is the queue is empty"""
        return self._size == 0 
    
    def first(self):
        """Returns but do not remove the first element of the queue"""
        if self.is_empty():
            raise Empty("Queue is Empty")
        head = self._tail._next
        return head._element 

    def dequeue(self):
        """Remove and returns the first element of the list"""
        if self.is_empty():
            raise Empty("queue is Empty")

        oldhead = self._tail._next
        if self._size == 1: #removing only element 
            self._tail = None 
        else:
            self._tail._next = oldhead._next 
        self._size -= 1 
        return oldhead._element 

    def enqueue(self, e):
        """Add an element to the back of the queue """
        newest = self._Node(e, None ) #new node will be a new tail node 
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next 
            self._tail._next = newest

        self._tail = newest
        self._size += 1 

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next #old head becomes new tail 
            
















        