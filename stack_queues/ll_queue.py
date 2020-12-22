#Implemnting queue ADT using singly linked list 

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""

    class Empty(Exception):
        """Error attempting to access an element from an empty container"""
        pass


    class _Node:
        """Lightweight, nonpublic class for storing singly linked node """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._elment = element
            self._next = next 

        def __init__(self):
            #create an empty queue 
            self._head = None
            self._tail = None 
            self._size = 0
        
        def __len__(self):
            #retuns size of the queue 
            return self._size 
        
        def is_empty(self):
            #returns true if the list is empty 
            return self._size == 0

        def first(self):
            #return but do not remove the top element of the queue 
            if self.is_empty():
                raise Empty('queue is empty')
            return self._head._element

        def dequeue(self):
            #remove and returns the first the element of the queue 
            if self.is_empty():
                raise Empty('Queue is empty')
            answer = self._head._element
            self._head = self._head._element
            self._size -= 1 
            if self.is_empty():
                self._tail = None 
            return answer 

        def enqueue(self, e):
            #add an element to the back of the queue 
            newest = self._Node(e, None) #this node will be a new tail node 
            if self.is_empty():
                self._head = newest
            else:
                self._tail._next = newest

            self._tail = newest
            self._size += 1 
            

