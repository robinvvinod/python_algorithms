class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SLL():
    def __init__(self):
        self.first = None

    def insertFront(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def insertBack(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            cur = self.first
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    def exists(self, data):
        if self.first is None:
            return False
        else:
            cur = self.first
            while (cur is not None) and (cur.data is not data):
                cur = cur.next

            if cur is None:
                return False
            return True

    def delete(self, data):
        if self.exists(data):
            cur = self.first
            if cur.data is data:
                self.first = cur.next
                return True
            while cur.next.data is not data:
                cur = cur.next
            cur.next = cur.next.next
            return True
        else:
            return False

    def __str__(self):
        if self.first is None:
            return None
        else:
            cur = self.first
            res = ""
            while cur is not None:
                res += str(cur.data) + '\n'
                cur = cur.next
            return res
