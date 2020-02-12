from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:
    def levelOrderBottom(self, root: TreeNode):
        queue = Queue()
        queue.put_nowait(root)
        orders = list()
        if root is None:
            return orders
        while queue.empty() is False:
            level_queue = Queue()
            level = list()
            while queue.empty() is False:
                cursor = queue.get_nowait()
                if cursor is None:
                    continue
                level.append(cursor.val)
                level_queue.put_nowait(cursor.left)
                level_queue.put_nowait(cursor.right)
            if level:
                orders.append(level)
            queue = level_queue
        return orders[::-1]
