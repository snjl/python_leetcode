import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder1(self, root: 'Node'):
        result = list()
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node is None:
            return None
        result.append(node.val)
        for child in node.children:
            self.helper(child, result)



    def preorder(self, root: 'Node'):
        result = list()
        stack = list()
        stack.append(root)
        if root is None:
            return result
        while stack:
            cursor = stack.pop()
            if cursor is None:
                continue
            result.append(cursor.val)
            stack.extend(cursor.children[::-1])
        return result

