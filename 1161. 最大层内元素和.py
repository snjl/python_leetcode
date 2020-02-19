# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_layer_num = 1
        now_layer_num = 0
        max_num = root.val
        import collections
        q = collections.deque()
        q.appendleft(root)
        while q:
            size = len(q)
            num = 0
            now_layer_num += 1
            for _ in range(size):
                cursor = q.pop()
                num += cursor.val
                if cursor.left:
                    q.appendleft(cursor.left)
                if cursor.right:
                    q.appendleft(cursor.right)
            if num > max_num:
                max_num = num
                max_layer_num = now_layer_num
        return max_layer_num





