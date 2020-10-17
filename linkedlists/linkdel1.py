#Python program to delete a node, given at a specific location in a linked list 

#Node class

class Node:

    #constructure to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#linkedlist class

class LinkedList:


    def __init__(self):
        self.head = None

        #function to insert new node at begning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


        #delete the first occurance of the given key in the linked list given
        #given reference of the head

    def deleteNode(self, key):

            #store head element 
        temp = self.head

            #if head node itself contains the element to be deleted 
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            #if key is not present in linked list
        if(temp == None):
            return

            #unlink the node from linked list
        prev.next = temp.next
        temp = None

            #utility function to print the linked list

    def printList(self):
        temp = self.head
        while(temp):
            print(" %d" %(temp.data)),
            temp = temp.next




#driver function 
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()














