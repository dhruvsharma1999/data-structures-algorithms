# Inserting a new node in DLL at end
# 7 step procedure

#Node class
class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev 
        self.data = data

#DLL class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):

        #1. allocate new node 2. put in the data
        new_node = Node(data = new_data)
        last = self.head

        #3. make next of last node as null, as it will be inserted at end
        new_node.next = None

        #4. is list is empty make new node as head of the list
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        #5. else traverse till the last point

        while (last.next is not None):
            last = last.next

        #6. change the next of last node
        last.next = new_node

        #change prev of new node
        new_node.pev = last

