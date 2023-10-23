class Stack:
    def __init__(self) -> None:
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

class QueueStack:
    def __init__(self) -> None:
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, element):
        self.in_stack.push(element)

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result


class AnimalShelter:
    '''
    An animal shelter operating strictly on “First-In/First-Out” basis
    holds only dogs and cats. People can select either a dog or a cat
    (and will recieve the oldest animal, based on arrival, of that type)
    or can take the oldest animal. Design a data structure to maintain
    this system, which includes functions such as enqueue,
    dequeueAny, dequeueDog, and dequeueCat.
    '''
    def __init__(self) -> None:
        self.cats = []
        self.dogs = []

    def __str__(self) -> str:
        return (f"{' '.join([ str(cat) for cat in self.cats])}"
                f" {' '.join([ str(dog) for dog in self.dogs])}"
                )

    def enqueue(self, animal, animal_type):
        ''' Adding the animal based on the type '''
        if animal_type == 'cat':
            self.cats.append(animal)
        if animal_type == 'dog':
            self.dogs.append(animal)
        return 'Not a valid animal type!'

    def dequeue_dog(self):
        ''' Get the dog which came in first '''
        if not self.dogs:
            return 'No dog available!'
        return self.dogs.pop(0)

    def dequeue_cat(self):
        ''' Get the cat which came in first '''
        if not self.cats:
            return 'No cat available!'
        return self.cats.pop(0)

    def dequeue_any(self):
        ''' Get any animal '''
        if not self.cats:
            return self.dogs.pop(0)
        return self.cats.pop(0)

temp_queue = AnimalShelter()
temp_queue.enqueue('Cat1', 'cat')
temp_queue.enqueue('Cat2', 'cat')
temp_queue.enqueue('Dog1', 'dog')
temp_queue.enqueue('Cat3', 'cat')
temp_queue.enqueue('Dog2', 'dog')
print(temp_queue)
