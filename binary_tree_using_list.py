''' Creation of Binary Tree built using List
In python, a Binary tree can be implemented with the use of the list data structure as well.
To initialize a binary tree using a list,
we first create an empty list to store the nodes of the tree. The first node of the tree is
left empty for better mathematical calculations.
'''

class BinaryTree:
    ''' A simple binary tree using a list '''
    def __init__(self, size) -> None:
        self.tree_list = size * [None]
        self.last_index_used = 0
        self.max_size = size

binary_tree = BinaryTree(10) # Creating O(N) for space and O(1) for time
