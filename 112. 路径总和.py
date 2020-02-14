class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        stack = list()
        if root is None:
            return False
        stack.append((root, 0))
        while len(stack):
            cursor, count = stack.pop()
            if cursor is None:
                continue
            count += cursor.val
            if count == sum and cursor.left is None and cursor.right is None:
                return True

            stack.append((cursor.left, count))
            stack.append((cursor.right, count))

        return False

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


