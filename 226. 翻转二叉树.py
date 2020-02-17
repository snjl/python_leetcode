# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        # 放在两个if上面也可以，相当于先交换再去递归
        root.left,root.right = root.right,root.left

        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        import collections
        q = collections.deque()
        q.appendleft(root)
        while q:
            t = q.pop()
            t.left,t.right = t.right,t.left
            if t.left:
                q.appendleft(t.left)
            if t.right:
                q.appendleft(t.right)


        return root
