# use self.check instead of this method
class queue():
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.array = [None for i in range(size)]

    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return self.head == (self.tail + 1) % self.size

    def enqueue(self, data):
        if self.isFull():
            print('Queue is full')
        else:
            if self.isEmpty():
                self.head = 0
                self.tail = 0
                self.array[self.tail] = data
            else:
                self.tail = (self.tail + 1) % self.size
                self.array[self.tail] = data

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            if self.head == self.tail:
                x = self.array[self.head]
                self.head = -1
                self.tail = -1
                return x

            x = self.array[self.head]
            self.head = (self.head + 1) % self.size

            return x
