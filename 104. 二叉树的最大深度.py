# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一 递归
class Solution1:
    def maxDepth(self, root):
        if not root:
            return 0
        max_l = self.maxDepth(root.left)  # 左子树的最大深度
        max_r = self.maxDepth(root.right)  # 右子树的最大深度
        return max(max_l, max_r) + 1  # 深度加上根节点


# 方法二 迭代
class Solution:
    """
    迭代法
    """

    def maxDepth(self, root):
        stack = []  # 定义一个空栈，栈中的元素是结点及其对应的深度
        if root:  # 如果根结点不为空
            stack.append((root, 1))  # 则将根节点及其对应深度1组成的元组入栈
        max_depth = 0  # 初始化最大深度为零
        while stack:  # 当栈非空时
            tree_node, cur_depth = stack.pop()  # 弹出栈顶结点及其对应的深度
            if tree_node:  # 如果该结点不为空
                max_depth = max(max_depth, cur_depth)  # 更新当前最大深度，如果该结点深度更大的话
                stack.append((tree_node.left, cur_depth + 1))  # 将该结点的左孩子结点及其对应深度压入栈中
                stack.append((tree_node.right, cur_depth + 1))  # 将该结点的右孩子结点及其对应深度压入栈中
        return max_depth

import collections

# 方法三 BFS
class Solution2:
    """
    迭代法
    """

    def maxDepth(self, root):
        depth = 0
        if root is None:
            return depth
        queue = collections.deque()
        queue.appendleft(root)
        while len(queue) != 0:
            reached = False
            depth += 1
            queue_len = len(queue)
            for i in range(queue_len):
                cursor = queue.pop()
                if cursor is None:
                    break
                if cursor.left:
                    queue.appendleft(cursor.left)
                if cursor.right:
                    queue.appendleft(cursor.right)
            if reached is True:
                break
        return depth


if __name__ == '__main__':
    x = Solution1()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t2.left = t3
    print(x.maxDepth(t1))
