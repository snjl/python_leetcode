
# Definition for a Node.
from queue import Queue


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node'):
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
                level.append(cursor.val)
                [level_queue.put_nowait(i) for i in cursor.children]
            orders.append(level)
            queue = level_queue
        return orders


if __name__ == '__main__':
    x = Solution()
    print(x.levelOrder(None))