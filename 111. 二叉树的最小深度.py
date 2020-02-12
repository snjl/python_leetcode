# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if root is None:
            return depth
        queue = collections.deque()
        queue.appendleft(root)
        while len(queue) != 0:
            reached = False
            depth += 1
            queue_len = len(queue)
            for i in range(queue_len):
                cursor = queue.pop()
                if cursor.left is None and cursor.right is None:
                    reached = True
                    break
                if cursor.left:
                    queue.appendleft(cursor.left)
                if cursor.right:
                    queue.appendleft(cursor.right)
            if reached is True:
                break
        return depth
