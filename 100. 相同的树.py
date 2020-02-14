class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        p_s = list()
        q_s = list()

        p_s.append(p)
        q_s.append(q)
        while p_s and q_s:
            pp = p_s.pop()
            qq = q_s.pop()
            if pp is None and qq is None:
                continue
            if pp is None or qq is None:
                return False
            if pp.val != qq.val:
                return False
            p_s.append(pp.left)
            p_s.append(pp.right)
            q_s.append(qq.left)
            q_s.append(qq.right)
        return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False