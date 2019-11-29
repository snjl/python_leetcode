# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head

        l =0
        h = head
        while h.next:
            h = h.next
            l += 1
        l += 1
        h.next = head
        # 旋转步数求余数，为真实旋转步数
        k = k % l
        k = l -k
        for i in range(k):
            h = h.next
            head = head.next
        h.next = None
        return head



