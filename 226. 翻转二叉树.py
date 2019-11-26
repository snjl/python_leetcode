# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        if root.right and root.left:
            root.right.val,root.left.val = root.left.val,root.right.val
        elif root.right:
            root.left = TreeNode(root.right.val)
            root.right = None
        elif root.left:
            root.right = TreeNode(root.left.val)
            root.left= None
        return root