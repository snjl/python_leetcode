class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum1(self, root: TreeNode, sum_: int):
        paths = list()
        stack = list()
        if root is None:
            return paths
        stack.append((root, [root.val]))
        while len(stack):
            cursor, path = stack.pop()

            if not cursor.right and not cursor.left and sum(path) == sum_:
                paths.append(path)
            if cursor.left:
                stack.append((cursor.left, path+[cursor.left.val]))
            if cursor.right:
                stack.append((cursor.right, path+[cursor.right.val]))


        return paths



    def pathSum(self, root: TreeNode, sum_: int):
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)

        res = []
        helper(root, [], sum_)
        return res




