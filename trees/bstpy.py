#implementing Binary search tree in python3 
#Node class
class Node:
    """Initiate the root node, with left and right child with value of None"""
    def __init__(self, value=None):
        self.value = value
        self.left_child  = None 
        self.right_child = None
    
class binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root) #setting a recursive function is root node is not empty

    def _insert(self, value, cur_node):
        """a private function which insert a new node in the BST if the root is not none"""
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else: 
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value: #creating elif in case the value is same as the current node 
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in the tree")

    def print_tree(self):
        if self.root!= None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node): 
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

def fill_tree(tree,num_elems=100, max_int=500):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)

tree.print_tree()