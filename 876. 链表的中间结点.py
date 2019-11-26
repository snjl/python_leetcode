# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = 0
        h = head
        while h:
            l += 1
            h = h.next
        if l % 2 == 1:
            l = (l + 1) // 2
        else:
            l = l // 2 + 1

        l = int(l)
        for i in range(l - 1):
            head = head.next

        return head

    def middleNode2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
