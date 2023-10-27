''' Creating a Queue using a linked list class '''

class Node:
    ''' A Node has a value and a pointer to the next node '''
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    ''' The Linked list => head and tail and a pointer to next
    '''
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        if not self.head:
            print('Empty Linkedlist')
        while self.head:
            yield self.head
            self.head = self.head.next

# Create the Queue
class Queue:
    ''' The Queue uses the First In First Out => FiFO procedure
    Create() the Queue, is_empty(), is_full(), enqueue(), dequeue(), peek()
    delete()
    
    '''
    def __init__(self) -> None:
        self.linked_list = LinkedList() # Initialize the linked list

    def __str__(self) -> str:
        return ' '.join([ str(element) for element in self.linked_list ])

    def is_empty(self):
        ''' Checks if a  queue is empty'''
        return not self.linked_list.head

    def peek(self):
        ''' Gets the top element in the list => the head '''
        if self.is_empty():
            return 'The Queue is empty!'
        return self.linked_list.head

    def delete(self):
        ''' To delete the elements , set the head and tail to None'''
        if self.is_empty():
            return ' The queue is already empty'
        self.linked_list.head = None
        self.linked_list.tail = None
        return 'Delete success!'

    def enqueue(self, value):
        ''' Add an element to the end of the queue '''
        new_node = Node(value)
        if self.is_empty():
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        self.linked_list.tail.next = new_node
        self.linked_list.tail = new_node

    def dequeue(self):
        ''' remove the first element of the queue '''
        if self.is_empty():
            return ' The queue is empty'
        current_node = self.linked_list.head  # The Head is the  current node
        if current_node == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
        self.linked_list.head = self.linked_list.head.next
        return current_node

# Create the Tree class

class TreeNode:
    ''' Creating a basic tree node '''
    def __init__(self, data) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None


# The Tree traversal
def preorder_traversal(root_node):
    ''' Taking the root node, check if the node is none( Tree is empty),
    print the root node
    call the recursive function on the left and right children
    
    Root => Left => Right
    '''
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

def inorder_traversal(root_node):
    ''' The inorder traversal => go through the Left subtree, then the root node then
    the right subtree recursively
    Left => Root => Right
    '''
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)

def post_order_traversal(root_node):
    ''' The post order traversal
    Left => Right => Root 
    '''
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


# The Breath First Traversal -> Level order traversal

def level_order_traversal(root_node):
    ''' Get all the nodes at levels'''
    if not root_node:
        return
    print(root_node.data)
    temp_queue = Queue()
    # Add the root node => level 1
    temp_queue.enqueue(root_node)
    while not temp_queue.is_empty():
        print('added success')
        root = temp_queue.dequeue()
        print(root.data)
        if root.data.left_child:
            temp_queue.enqueue(root.data.left_child)
        if root.data.right_child:
            temp_queue.enqueue(root.data.right_child)

new_tree = TreeNode('Drinks')
print(new_tree.data)
left_child = TreeNode('Hot')
tea = TreeNode('latte')
coffee = TreeNode('Mocha')
left_child.left_child = tea
left_child.right_child = coffee

right_child = TreeNode('Cold')
coke = TreeNode('Coke')
sprite = TreeNode('Sprite')
right_child.left_child = coke
right_child.right_child = sprite

new_tree.left_child = left_child
new_tree.right_child = right_child

preorder_traversal(new_tree)

print('\n The inorder traversal \n')
inorder_traversal(new_tree)
print('\n The inorder traversal \n')
post_order_traversal(new_tree)

print('**************8The Breadh Fisrt Traversal ********\n')
level_order_traversal(new_tree)

# Insert the node

def insert_node(root_node, new_node):
    ''' Insert a node to the tree'''
    if not root_node:
        root_node = new_node
    temp_queue = Queue()
    temp_queue.enqueue(root_node)
    while not temp_queue.is_empty():
        root = temp_queue.dequeue()
        if root.data.left_child:
            temp_queue.enqueue(root.data.left_child)
            root.data.left_child = new_node
            return 'added successfully!'
        if root.right_child:
            temp_queue.enqueue(root.data.right_child)
            root.data.right_child = new_node
            return 'Node successfully added!'

def search_binary_tree(root_node, element_to_find):
    ''' Serach for an element in the binary tree '''
    if not root_node:
        return 'Empty Binary tree'
    temp_queue = Queue()
    temp_queue.enqueue(root_node)
    while not temp_queue.is_empty():
        root = temp_queue.dequeue()
        if root.data == element_to_find:
            return 'The element was found'
        if root.data.left_child:
            temp_queue.enqueue(root.data.left_child)
        if root.data.right_child:
            temp_queue.enqueue(root.data.right_child)
    return 'Element Not found'

def delete_the_tree(root_node):
    ''' Delete the tree '''
    if not root_node:
        return 'We can not delete an empty tree'
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return 'The Binary Tree has been successfully deleted'
