import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        view = list()
        if root is None:
            return view
        q = collections.deque()
        q.appendleft(root)
        while len(q):
            size = len(q)
            # 最后一个才存储值
            l = list()
            for i in range(size):
                cursor = q.pop()
                if cursor is None:
                    continue
                l.append(cursor.val)
                q.appendleft(cursor.left)
                q.appendleft(cursor.right)
            if len(l):
                view.append(l[-1])
        return view




