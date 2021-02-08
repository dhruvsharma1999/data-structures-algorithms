#implementing priority queue 
class PriorityQueueBase:
    """abstract base class for a priority queue"""

    class _item:
        """lightweight class to store priority queue item"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v 

        def __it__(self, other):
            return self._key < other._key #comparing items based on their keys

        def is_empty(self):
            """Return true if priority queue is empty"""
            return len(self) == 0