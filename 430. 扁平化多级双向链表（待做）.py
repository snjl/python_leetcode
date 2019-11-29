class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        h = head
        while h:
            # 如果没有child节点
            if h.child is None:
                h = h.next
            # 如果有child节点，递归调用
            else:
                # 存储下一个节点
                n = h.next
                h = h.child
                while h:
                    h = h.next
                h.next = n
        return head

    def child_flatten(self,head):
        pass