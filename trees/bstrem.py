#python program to remove a given node from the BST

#Node class
class Node:
    def __init__(self, key):
        self.right = None
        self.left = None 
        self.key = key

#utility function for inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

#utility function to insert a new node in BST 
def insert(node, key):
    #if tree is empty return the node

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

#in a given BST, return the node with minimum value
def minValueNode(node):
    current = node

    #looping down to find the left most element
    while(current.left is not None):
        current = current.left

    return current 

# Given a binary search tree and a key, the following function
# will delete the key and returns the new root
#

def deleteNode(root, key):

    #base case
    if root is None:
        return root

    #if key to be deleted is smaller than the root key
    if key < root.key:
        root.left = deleteNode(root.left, key)

    #if the key to be deleted is larger than the root key
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    
    #if key is same as root's key then this is the node that needs to be
    #deleted

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        if root.right is None:
            temp = root.left
            root = None
            return temp
    
    #Node with two children
    #get inorder succersor i.e smallest in the right subtree

        temp = minValueNode(root.right)

    #copyt the inorder successor content to this node

        root.key = temp.key

    #finding and deleting the inorder successor
        root.right = deleteNode(root.right, temp.key)

    
    return root


root = None
root = insert(root, 50)

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree:")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of modified tree:")
inorder(root)
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of modified tree:")
inorder(root)


















































