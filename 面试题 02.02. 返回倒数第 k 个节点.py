# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        l = 0
        h = head
        while h is not None:
            h = h.next
            l += 1

        num = l - k
        for i in range(num):
            head = head.next

        return head.val



