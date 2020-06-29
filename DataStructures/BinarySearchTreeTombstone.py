class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.tombstone = False

    def __str__(self):
        return "{0:<10}{1:<10}{2:<10}".format(self.data, self.left, self.right)


class BST():
    def __init__(self):
        self.root = None

    def findMax(self, cur):
        if cur:
            res = cur.data
            rightMax = self.findMax(cur.right)
            leftMax = self.findMax(cur.left)
            if leftMax:
                res = max(res, leftMax)
            if rightMax:
                res = max(res, rightMax)
            return res
        else:
            return None

    def findMin(self, cur):
        if cur:
            res = cur.data
            rightMin = self.findMin(cur.right)
            leftMin = self.findMin(cur.left)
            if rightMin:
                res = min(res, rightMin)
            if leftMin:
                res = min(res, leftMin)
            return res
        else:
            return None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertRecursive(data, self.root)

    def insertRecursive(self, data, cur):

        if cur.tombstone and (
            self.findMin(cur.right) >= data and self.findMax(cur.left) < data
        ):
            cur.tombstone = False
            cur.data = data

        if data < cur.data:
            if cur.left is None:
                cur.left = Node(data)
            else:
                self.insertRecursive(data, cur.left)
        else:
            if cur.right is None:
                cur.right = Node(data)
            else:
                self.insertRecursive(data, cur.right)

    def findTarget(self, data):
        if self.root is None:
            return None
        else:
            self.findTargetRecursive(data, self.root)

    def findTargetRecursive(self, data, cur):
        if data == cur.data and cur.tombstone is False:
            return cur
        elif data < cur.data:
            if cur.left is None:
                return None
            else:
                self.findTargetRecursive(data, cur.left)
        else:
            if cur.right is None:
                return None
            else:
                self.findTargetRecursive(data, cur.right)

    def exists(self, data):
        return self.findTarget(data) is not None

    def delete(self, data):
        target = self.findTarget(data)
        if target is None:
            return False
        else:
            target.tombstone = True
            return True

    def traversal(self, mode):
        if mode == "pr":
            self.preOrder(self.root)
        elif mode == "in":
            self.inOrder(self.root)
        else:
            self.postOrder(self.root)

    def preOrder(self, cur):
        if cur:
            print(cur.data)
            print(self.preOrder(cur.left))
            print(self.preOrder(cur.right))

    def inOrder(self, cur):
        if cur:
            print(self.inOrder(cur.left))
            print(cur.data)
            print(self.inOrder(cur.right))

    def postOrder(self, cur):
        if cur:
            print(self.postOrder(cur.left))
            print(self.postOrder(cur.right))
            print(cur.data)
