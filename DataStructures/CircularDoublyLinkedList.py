class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class CDLL():
    def __init__(self):
        self.first = None

    def insertFront(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.first.next = newNode
            self.first.prev = newNode
        else:
            newNode.next = self.first
            newNode.prev = self.first.prev
            newNode.prev.next = newNode
            self.first.prev = newNode
            self.first = newNode

    def insertBack(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.first.next = newNode
            self.first.prev = newNode
        else:
            current = self.first
            while current.next is not self.first:
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = self.first
            self.first.prev = newNode

    def exists(self, data):
        if self.first is None:
            return False
        else:
            current = self.first
            while current.data is not data:
                current = current.next
                if current is self.first:
                    return False
            return True

    def delete(self, data):
        if self.exists(data):
            current = self.first

            if self.first.data is data:
                self.first = current.next
                self.first.prev = current.prev
                current.prev.next = self.first
                return True

            while current.data is not data:
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            return True
        else:
            return False

    def __str__(self):
        if self.first is None:
            return None
        else:
            result = ''
            current = self.first
            while True:
                result += str(current) + '\n'
                current = current.next
                if current == self.first:
                    break
            return result
