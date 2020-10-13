# A complete working python program to demonstrate all
# inertion methods of linked list
#
# Node class
class Node:
    #function to initialize the node object
    def __init__(self, data):
        self.data = data    # assign data
        self.next = None    # initialize next as null

# Linked list class contains a Node object
class LinkedList:
    
    #function to initialize the head
    def __init__(self):
        self.head = None

    #function to insert a new node at the beginning
    def push(self, new_data):
        
        #allocate the node and put in the data
        new_node = Node(new_data)
        
        #make next of new node as head
        new_node.next = self.head

        #move the head to point  to new node
        self.head = new_node

    # Insert a new node after the given previous node (prev_node)
    #

    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exist
        if prev_node is None:
            print("The given previous node must be in linked list")
            return

        # 2. create a new node and insert the data
        new_node = Node(new_data)
        # 4. make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 5.make next of prev node as new_node
        prev_node.next = new_node


        # function to append new node at the end of the list
    def append(self, new_data):
        new_node = Node(new_data)

            #if the linked list is empty make the new node as head

        if self.head is None:
            self.head = new_node
            return

            # else traverse till last node
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node


            #utility function to print the linked list 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# code execution
#
if __name__ =='__main__':

    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)

    llist.insertAfter(llist.head.next, 8)

    print("Created linked list is: ")
    llist.printList()

    













