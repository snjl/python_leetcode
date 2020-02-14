class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths1(self, root: TreeNode):
        paths = list()
        stack = list()
        if root is None:
            return paths
        stack.append((list(), root))
        while stack:
            path, cursor = stack.pop()
            p = path[::]

            if cursor is None:
                continue
            p.append(cursor.val)

            if cursor.left is None and cursor.right is None:
                paths.append(p)
                continue

            stack.append((p, cursor.left))
            stack.append((p, cursor.right))

        str_paths = list()
        for path in paths:
            str_paths.append('->'.join([str(i) for i in path]))
        return str_paths

    def binaryTreePaths(self, root: TreeNode):
        paths = list()

        self.helper(root, list(), paths)

        str_paths = list()
        for path in paths:
            str_paths.append('->'.join([str(i) for i in path]))
        return str_paths

    def helper(self, node, path, paths):
        if node is None:
            return
        p = path[::]
        p.append(node.val)

        if node.left is None and node.right is None:
            paths.append(p)
            return
        self.helper(node.left, p, paths)
        self.helper(node.right, p, paths)
