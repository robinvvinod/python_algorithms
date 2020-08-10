class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return '{0:<10}{1:<10}{2:<10}'.format(self.data, self.left, self.right)


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertRecursive(data, self.root)

    def insertRecursive(self, data, cur):

        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self.insertRecursive(data, cur.left)
        else:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self.insertRecusrive(data, cur.right)

    def insertIterative(self, data):
        cur = self.root
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = Node(data)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(data)
                    break
                cur = cur.right

    def exists(self, data):
        if self.root is None:
            return None
        else:
            self.existsRecursive(data, self.root)

    def existsRecursive(self, data, cur):
        if data is cur.data:
            return True

        if data < cur.data:
            if cur.left is None:
                return False
            self.existsRecursive(data, cur.left)
        else:
            if cur.right is None:
                return False
            self.existsRecursive(data, cur.right)

    def existsIterative(self, data):
        cur = self.root
        while True:
            if data is cur.data:
                return True
            else:
                if data < cur.left:
                    if cur.left is None:
                        return False
                    cur = cur.left
                else:
                    if cur.right is None:
                        return False
                    cur = cur.right

    def traversal(self, mode):
        if mode == "pr":
            self.preOrder(self.root)
        elif mode == "po":
            self.postOrder(self.root)
        else:
            self.inOrder(self.root)

    def preOrder(self, cur):
        if cur:
            print(cur.data)
            print(self.preOrder(cur.left))
            print(self.preOrder(cur.right))

    def postOrder(self, cur):
        if cur:
            print(self.postOrder(cur.left))
            print(self.postOrder(cur.right))
            print(cur.data)

    def inOrder(self, cur):
        if cur:
            print(self.inOrder(cur.left))
            print(cur.data)
            print(self.inOrder(cur.right))
