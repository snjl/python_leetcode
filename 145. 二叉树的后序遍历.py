
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def postorderTraversal1(self, root: TreeNode):
        l = list()
        self.helper(root, l)
        return l

    def helper(self, root, l):
        if root:
            self.helper(root.left, l)
            self.helper(root.right, l)
            l.append(root.val)



    # 染色方法
    def postorderTraversal2(self, root: TreeNode):
        stack = list()
        stack.append((0, root))
        result = list()
        while stack:
            color, cursor = stack.pop()
            if cursor is None:
                continue
            if color == 0:
                stack.append((1, cursor))
                stack.append((0, cursor.right))
                stack.append((0, cursor.left))

            else:
                result.append(cursor.val)
        return result

    # 迭代方法（看不懂）

    def postorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right  # 先将右节点压栈
            top = stack.pop()  # 此时该节点的右子树已经全部遍历完
            cur = top.left  # 对左子树遍历
        return res[::-1]  # 结果翻转
