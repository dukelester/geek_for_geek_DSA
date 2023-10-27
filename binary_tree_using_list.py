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

    # Insert into a Binary tree

    def insert_node(self, new_node):
        ''' Insert the new node to the binary Tree'''
        if self.last_index_used + 1 == self.max_size:
            return 'The tree is full'
        self.tree_list[self.last_index_used + 1] = new_node
        self.last_index_used += 1
        return 'The value was successfully added!'

    def search_for_node(self, node_value):
        '''Search for an element in a node '''
        for i, _ in enumerate(self.tree_list):
            if self.tree_list[i] == node_value:
                return 'Element Found'
        return 'Element can not be found'


binary_tree = BinaryTree(10) # Creating O(N) for space and O(1) for time
print(binary_tree.insert_node(34), binary_tree.insert_node(44), binary_tree.insert_node(30)) # O(1)
print(binary_tree.search_for_node(440))
print(binary_tree.search_for_node(44))
