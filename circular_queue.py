''' Has two pointers for the rear and front'''

class CircularQueue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.rear = -1
        self.front = -1

    def __str__(self) -> str:
        return ' '.join([ str(item) for item in self.items ])

    def is_full(self):
        if self.rear + 1 == self.front:
            return True
        if self.front == 0 and self.rear + 1 == self.max_size:
            return True
        return False


c_queue = CircularQueue(7)
print(c_queue)
print(c_queue.is_full())
