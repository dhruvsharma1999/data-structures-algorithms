# a python class that represents an individual node in a BINARY tree
#

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# creating root node
#
root = Node(1)

root.left = Node(2)
root.right = Node(3)

# 2 and 3 becomes left and right children of 1
#

root.left.left = Node(4)

#4 becomes left child of 2
