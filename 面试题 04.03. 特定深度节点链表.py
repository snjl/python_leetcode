import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode):
        layers = list()
        if tree is None:
            return layers
        q = collections.deque()
        q.appendleft(tree)
        while len(q):
            size = len(q)
            layer = ListNode(-1)
            header = layer
            for i in range(size):
                cursor = q.pop()
                if cursor is None:
                    continue
                header.next = ListNode(cursor.val)
                header = header.next
                q.appendleft(cursor.left)
                q.appendleft(cursor.right)
            # 说明已经有新值插入
            if header != layer:
                layer = layer.next
                layers.append(layer)
        return layers

