#Implementing stack using a singly linked list

class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage"""

    class Empty(Exception):
        """Error attempting to access an element from an empty container"""
    pass


    #nested node class
    class _Node:
        """Ligthweight, non public class for storing a singly linked node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next 

        #implementing stack method 
        def __init__(self):
            #Create an empty stack
            self._head = None
            self._size = 0

        def __len__(self):
            #return length of the list 
            return self._size

        def is_empty(self):
            #returns true if the size of the stack is 0
            return self._size == 0
        
        def push(self, e):
            #Add element e to the top of the stack
            self._head = self._Node(e, self._head)
            self._size += 1

        def top(self):
            #Returns but do not remove element at the top of the stack 
            if self.is_empty():
                raise Empty('Stack is Empty ')
            return self._head._element

        def pop(self):
            #Returns and remove element from the top of the stack 
            if self.is_empty():
                raise Empty('Stack is empty')
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1 
            return answer
