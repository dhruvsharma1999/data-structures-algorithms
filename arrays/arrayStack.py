"""
The adapter pattern for applying stack implementation in python using python 
List class as underlying storage"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class AarrayStack:
    """LIFO stack implementation using python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elments in the stack"""

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the list"""
        self._data.append(e)

    def top(self):
        """Returns (but do not remove) the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        """ Remove and return the element from the top of the stack

        Raise Empty exception is the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()
