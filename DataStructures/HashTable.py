class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]

    def insert(self, data):
        target = hash(data) % self.size
        end = target

        while self.array[target] is not None:
            target = (target + 1) % self.size
            if target == end:
                return "Hash table is full"

        self.array[target] = data

    def getIndex(self, data):
        target = hash(data) % self.size
        end = target
        while self.array[target] != data:
            target = (target + 1) % self.size
            if target == end:
                return -1
        return target

    def delete(self, data):
        target = self.getIndex(data)
        if target != -1:
            self.array[target] = None
        else:
            return False

    def exists(self, data):
        return not self.getIndex(data) == -1

    def __str__(self):
        res = ""
        for i in range(len(self.array)):
            res += str(i) + ": " + str(self.array[i])
        return res
