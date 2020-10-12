# implementation of linked list using python 3

# Node class
class Node:

    #function to initialize the node object
    def __init__(self, data):
        self.data = data #assign data
        self.next = None #initialize next as null

#Linked list class
class LinkedList:

    #function to initialize the linked 
    #list object

    def __init__(self):
        self.head = None


    #function to print the contents of linked list
    #starting from head

    def printingList(self):
    	temp = self.head
    	while (temp):
    		print (temp.data)
    		temp = temp.next



#code execution starts here

if __name__ == '__main__':

    #starts with empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    '''
    Three nodes have been created.
    We have reference to these blocks as
    head -> secong -> third
    '''

    llist.head.next = second; 
          
    second.next = third;

    llist.printingList()
















