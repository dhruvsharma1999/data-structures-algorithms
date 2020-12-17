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
    