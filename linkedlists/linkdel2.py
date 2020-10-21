#python program to delete a node in a linked list
#at a given location 

class Node:

    #constructor to initialize the node object
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:

    #constructor to initialize the head
    def __init__ (self):
        self.head = None

    #function to insert a new node at the begining
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of the a list
    # and a position, delete the node at a given position

    def deleteNode(self, position):

        #if linked list is empty
        if self.head == None:
            return
        #store head node

        temp = self.head
        
        #if head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        #find previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        #if position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        #Node temp.next is the node to be deleted
        #store pointer to the next of the node to be deleted

        next = temp.next.next

        #unlink the node from the linked list

        temp.next = None
        temp.next = next

    
    def printList(self):
        temp = self.head 
        while (temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created linked list:")
llist.printList()
llist.deleteNode(4)
print("\nLinked list after deletion at position 4:")
llist.printList()






















