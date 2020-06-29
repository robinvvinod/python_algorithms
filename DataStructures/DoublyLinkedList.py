class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class DLL():
    def __init__(self):
        self.first = None

    def insertFront(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first.prev = newNode
            self.first = newNode

    def insertBack(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def exists(self, data):
        if self.first is None:
            return False
        else:
            current = self.first
            while (current is not None) and (current.data is not data):
                current = current.next

            if current is None:
                return False
            else:
                return True

    def delete(self, data):
        if self.exists(data):
            current = self.first
            while current.data is not data:
                current = current.next

            if current.prev is None:  # Current is first
                self.first = current.next
                self.first.prev = None
            else:
                if current.next is not None:
                    current.next.prev = current.prev
                current.prev.next = current.next
            return True
        else:
            return False

    def __str__(self):
        if self.first is None:
            return None
        else:
            result = ''
            current = self.first
            while current is not None:
                result += str(current) + '\n'
                current = current.next
            return result
