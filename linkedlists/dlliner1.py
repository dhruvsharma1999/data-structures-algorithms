#python function implementing insertion in doubly linked list
# 1. insersiton of a node at the begining of the list
# 5 step procedure to add node at begining of the list

#node class
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.head = data

#push function to add node at the begining of the list
def push(self, data):

    #1 & 2 allocate the node and put in the data 
    new_node = Node(data= new_data)

    #make next of new node at head and prev as NULL
    new_node.next = self.head
    new_node.prev = None

    #chaning previous of head node as new node  
    if self.head is not None:
        self.head.prev = new_node

    #make self.head as new node
    self.head = new_node
