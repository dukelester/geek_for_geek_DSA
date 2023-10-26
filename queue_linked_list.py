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
