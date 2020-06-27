# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 边界条件不用忘记了
        if not (head and head.next):
            return True
        p = ListNode(-1)
        p.next, low, fast = head, p, p
        # 快慢指针不断迭代，找到中间节点
        while fast and fast.next:
            low, fast = low.next, fast.next.next
        cur, pre = low.next, None
        low.next = None
        # 将链表一分为二之后，反转链表后半部分
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        a, b = p.next, pre
        # 将链表前半部分和 反转的后半部分对比
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return True


