# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 记录链表长度
        l = 0
        h = head
        while h:
            h = h.next
            l += 1
        down = l - k

        h = head
        for i in range(down):
            h = h.next
        return h

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        # 记录链表长度
        h = head
        while head:
            if k > 0:
                k -= 1
            else:
                h = h.next
            head = head.next

        return h



if __name__ == '__main__':
    x = Solution()

    print(x.getKthFromEnd(None))
