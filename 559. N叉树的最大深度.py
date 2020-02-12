import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
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
                if cursor is None:
                    break
                for child in cursor.children:
                    queue.appendleft(child)
            if reached is True:
                break
        return depth




