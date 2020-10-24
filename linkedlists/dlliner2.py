#implementing node at insertion in a doubl linked list
# 2. Adding a node after a given node a 7 steps process

class Node:
    def __init__(self, next = None, prev = None, data = None):
        self.next = next
        self.prev = prev
        self.data = data

#doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAfter(self, prev_node, new_data):

    # 1. check if the given prev_node is NULL
        if prev_node = None:
            print("This node is doesn't exist in DLL")
            return

    # 2. allocate node and 3. put in the data
        new_node = node(data = new_data)

    # 4. make next of new node as next of prev node
        new_node.next = prev_node.next

    # 5. make next of prev node as new node
        prev_node.next = new_node

    # 6. make previous node at previous of new node
        new_node.prev = prev_node

    # 7. change previous of NEW node's NEXT node
        if new_node.next is not None:
            new_node.next.prev = new_node
