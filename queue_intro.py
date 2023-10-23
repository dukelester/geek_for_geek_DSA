''' Create a Queue '''

class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        return ' '.join([ str(item) for item in self.items ])

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)
        return self.items

    def dequeue(self):
        if self.is_empty():
            return ' The Queue is empty we can not remove!'
        removed = self.items.pop(0)
        return f'{removed} was removed from the queue:  {self.items}'

    def peek(self):
        if self.is_empty():
            return ' The Queue is empty we can not get peek!'
        return self.items[0]
    def delete(self):
        self.items = None
        return self.items

bank_queue = Queue()
print(bank_queue.is_empty())
bank_queue.enqueue(87993)
bank_queue.enqueue(34)
bank_queue.enqueue(89)
bank_queue.enqueue(4590)
bank_queue.enqueue(23114)
print(bank_queue)

print(bank_queue.dequeue())
print(bank_queue.is_empty())
print(bank_queue.peek())
print(bank_queue.delete())
