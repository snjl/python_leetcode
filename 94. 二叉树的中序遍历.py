# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def inorderTraversal1(self, root: TreeNode):
        nums = []
        return self.method(root, nums)

    def method(self, root: TreeNode, nums):
        if root is not None:
            self.method(root.left, nums)
            nums.append(root.val)
            self.method(root.right, nums)
            return nums

    # 栈
    def inorderTraversal2(self, root: TreeNode):
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    # 染色方法
    def inorderTraversal(self, root: TreeNode):
        stack = list()
        stack.append((0, root))
        result = list()
        while stack:
            color, cursor = stack.pop()
            if cursor is None:
                continue
            if color == 0:
                stack.append((0, cursor.right))
                # 染色为1，表示已经到过该节点，下一次路过取出value进行存储
                stack.append((1, cursor))
                # 由于使用栈，所以这里倒序，这样会从左节点开始取出
                stack.append((0, cursor.left))
            else:
                result.append(cursor.val)

        return result


if __name__ == '__main__':
    x = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    x.inorderTraversal(a)
    print(x.inorderTraversal(a))
