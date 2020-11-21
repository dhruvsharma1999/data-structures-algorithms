#implementing bst search operation using python 3

#Node class
class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key

#Utility function to search a given key in BST
    def search(root, key):

        #base case is root is NULL or key is present at the root
        if root is None or root.val == key:
            return root

        #if key greater than roots key
        if root.val < key:
            return search(root.right, key)

        #if key is smaller than root key 
        return search(root.left, key)
