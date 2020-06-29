class Stack():
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.array = [None for i in range(size)]

    def isEmpty(self):
        return self.top < 0

    def isFull(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.isFull():
            print('Stack is already full')
        else:
            self.top += 1
            self.array[self.top] = data

    def pop(self):
        if self.isEmpty():
            print('Stack is already empty')
        else:
            self.top -= 1
            return self.array[self.top + 1]
