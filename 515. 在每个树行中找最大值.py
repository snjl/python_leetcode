# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):
        layers = list()
        q = collections.deque()
        q.appendleft(root)
        while len(q):
            size = len(q)
            # 最后一个才存储值
            m = None
            for i in range(size):
                cursor = q.pop()
                if cursor is None:
                    continue
                if m is None:
                    m = cursor.val
                else:
                    if cursor.val > m:
                        m = cursor.val
                if cursor.left:
                    q.appendleft(cursor.left)
                if cursor.right:
                    q.appendleft(cursor.right)
            if m is not None:
                layers.append(m)
        return layers


