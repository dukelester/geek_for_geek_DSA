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

    # Preoder traversal ===> Root => Left Subtree => Right Subtree
    def preorder_traversal(self, index):
        ''' Get the elements starting with the root, then left subtree and the right subtree'''
        if index > self.last_index_used:
            return
        print(self.tree_list[index])
        self.preorder_traversal(index * 2)
        self.preorder_traversal(index * 2 + 1)

    def inorder_traversal(self, index):
        ''' Get the left subtree, then the root and then the right subtree'''
        if index > self.last_index_used:
            return
        self.inorder_traversal(index * 2)
        print(self.tree_list[index])
        self.inorder_traversal(index * 2 + 1)


    def postorder_traversal(self, index):
        ''' Get the left subtree => get the right subtree => Root'''
        if index > self.last_index_used:
            return
        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.tree_list[index])



binary_tree = BinaryTree(10) # Creating O(N) for space and O(1) for time
print(binary_tree.insert_node(34), binary_tree.insert_node(44), binary_tree.insert_node(30)) # O(1)
print(binary_tree.search_for_node(440))
print(binary_tree.search_for_node(44))
binary_tree.insert_node(23)
binary_tree.insert_node(67)
binary_tree.insert_node(68)
binary_tree.insert_node(90)
binary_tree.preorder_traversal(1)
print('\ninorder traversal \n')
binary_tree.inorder_traversal(1)

print('\n postorder traversal \n')
binary_tree.postorder_traversal(1)
