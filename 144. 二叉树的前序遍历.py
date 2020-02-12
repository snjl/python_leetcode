class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def preorderTraversal1(self, root: TreeNode):
        l = list()
        self.helper(root, l)
        return l

    def helper(self, root, l):
        if root:
            l.append(root.val)
            self.helper(root.left, l)
            self.helper(root.right, l)

    # 染色方法
    def preorderTraversal2(self, root: TreeNode):
        stack = list()
        stack.append((0, root))
        result = list()
        while stack:
            color, cursor = stack.pop()
            if cursor is None:
                continue
            if color == 0:
                stack.append((0, cursor.right))
                stack.append((0, cursor.left))
                stack.append((1, cursor))

            else:
                result.append(cursor.val)
        return result

    # 迭代方法（看不懂）
    def preorderTraversal(self, root: TreeNode):
        res = []  # 结果列表
        stack = []  # 辅助栈
        cur = root  # 当前节点
        while stack or cur:
            while cur:  # 遍历到最后一层
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            top = stack.pop()  # 此时该节点的左子树已经全部遍历完
            cur = top.right  # 对右子树遍历
        return res


