# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if root is None:
            return 0
        import collections
        sum = 0
        q = collections.deque()
        q.appendleft(root)
        while q:
            t = q.pop()
            if t.left:
                if t.left.left is None and t.left.right is None:
                    sum += t.left.val
                q.appendleft(t.left)
            if t.right:
                q.appendleft(t.right)

        return sum