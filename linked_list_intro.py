# Create the Node => value and a pointer

class Node:
    ''' Linked list Node '''
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    ''' A simple singly linked list '''
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        head_node = self.head
        while head_node:
            yield head_node
            head_node = head_node.next

    def insert_at_beginning(self, data):
        ''' Insert the data at the beginning of the linked list '''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert_at_middle(self, mid_node, data):
        ''' Insert anywhere bewteen the list '''
        if mid_node is None:
            return
        new_node = Node(data)
        new_node.next = mid_node.next
        mid_node.next = new_node

    def insert_at_end(self, value):
        ''' Insert at the end of the linked list '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.tail = new_node

    def search_in_list(self, item):
        ''' Search for an element in a linked list '''
        if self.head is None:
            return 'Not found in an empty Linked list'
        position = 0
        found = 0
        current_node = self.head
        while current_node:
            position += 1
            if current_node.value == item:
                found = 1
            current_node = current_node.next
        if found:
            return f'Found at position {position}'
        return 'Not found'

    def reverse_linked_list(self):
        ''' Reverse the linked list '''
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev



linked_list = LinkedList()
head = Node(89)
linked_list.head = head
simple_node = Node(300)
linked_list.head.next = simple_node
print(simple_node.value, linked_list.head.value, linked_list.head.next.value)
print([ val.value for val in linked_list ])
linked_list.insert_at_beginning(90)
linked_list.insert_at_beginning(12)
# linked_list.insert_at_middle(89, 100)
print([ val.value for val in linked_list ])

print(linked_list.search_in_list(12))


# Remove duplicates from a linked list
def remove_duplicates(linked_list):
    ''' remove the duplicates from a linked list '''
    if linked_list.head is None:
        return 'Empty linked list'
    current_node = linked_list.head
    visited = set([current_node.value])

    while current_node.next:
        if current_node.next.value in visited:
            current_node.next = current_node.next.next
        visited.add(current_node.next.value)
        current_node = current_node.next
    return linked_list


def kth_to_last(linked_list, k):
    first_pointer = linked_list.head
    second_pointer = linked_list.head
    for _ in range(k):
        if second_pointer is None:
            return None
        second_pointer = second_pointer.next
    while second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return first_pointer

linked_list.reverse_linked_list()
