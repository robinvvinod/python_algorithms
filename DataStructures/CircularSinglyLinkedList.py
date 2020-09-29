class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CSLL():
    def __init__(self):
        self.first = None

    def insertFront(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.first.next = newNode
        else:
            cur = self.first
            while cur.next is not self.first:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.first
            self.first = newNode

    def insertBack(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.first.next = newNode
        else:
            cur = self.first
            while cur.next is not self.first:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.first

    def exists(self, data):
        if self.first is None:
            return False
        else:
            cur = self.first
            while (cur.next is not self.first) and (cur.data is not data):
                cur = cur.next
            if cur.data is not data:
                return False
            return True

    def delete(self, data):
        if self.exists(data):
            cur = self.first
            if cur.data is data:
                while cur.next is not self.first:
                    cur = cur.next
                cur.next = self.first.next
                self.first = self.first.next
            
            else:
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
            res = ''
            cur = self.first
            while True:
                res += str(cur) + '\n'
                cur = cur.next
                if cur == self.first:
                    break
            return res


LL = CSLL()
LL.insertFront(10)
LL.insertFront(20)
LL.insertBack(5)
print(LL)
