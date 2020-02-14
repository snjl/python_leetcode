import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:

        return self.isMirror(root, root)

    def isMirror(self, left, right):

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            if self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left):
                return True
            else:
                return False


    def isSymmetric(self,root):
        q = collections.deque()
        q.appendleft(root)
        q.appendleft(root)
        while len(q):
            left = q.pop()
            right = q.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            q.appendleft(left.left)
            q.appendleft(right.right)
            q.appendleft(left.right)
            q.appendleft(right.left)
        return True
