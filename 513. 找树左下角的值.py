import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        layers = list()
        q = collections.deque()
        q.appendleft(root)
        while len(q):
            size = len(q)
            # 最后一个才存储值
            layer = list()
            for i in range(size):
                cursor = q.pop()
                if cursor is None:
                    continue
                layer.append(cursor.val)
                q.appendleft(cursor.left)
                q.appendleft(cursor.right)
            if layer:
                layers.append(layer)
        return layers[-1][0]
