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
