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
