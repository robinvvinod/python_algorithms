# use self.check instead of this method
class queue():
    def __init__(self, size):
        self.size = size
        self.head = 0
        self.tail = 0
        self.array = [None] * (size + 1)

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.head == (self.tail + 1) % (self.size + 1)

    def enqueue(self, data):
        if self.isFull():
            print('Queue is full')
        else:
            self.array[self.tail] = data
            self.tail = (self.tail + 1) % (self.size + 1)

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            x = self.array[self.head]
            self.head = (self.head + 1) % (self.size + 1)

            return x
