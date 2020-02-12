import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        q = collections.deque()
        q.appendleft(root)
        flag = True
        result = list()
        while len(q) > 0:
            size = len(q)
            level_result = collections.deque()
            for i in range(size):
                cursor = q.pop()
                if cursor is None:
                    continue
                if flag:
                    level_result.append(cursor.val)
                else:
                    level_result.appendleft(cursor.val)
                q.appendleft(cursor.left)
                q.appendleft(cursor.right)
            if len(level_result) >0:
                result.append(level_result)
            flag = not flag
        return result
