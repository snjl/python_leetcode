class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ("->" if self.next is not None else "")

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        a = self
        while a:
            if a.next:
                print(a, end='')
            else:
                print(a)
            a = a.next

class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = ListNode(-1)
        odd_h = odd
        h = head
        even = ListNode(-1)
        even_h = even
        flag = 1
        while h:
            if flag == 1:
                odd_h.next = h
                odd_h = odd_h.next
            else:
                even_h.next = h
                even_h = even_h.next
            flag = flag ^ 1
            h = h.next
        odd_h.next = even.next
        even_h.next = None
        return odd.next


if __name__ == '__main__':


    head = ListNode(4)
    b = ListNode(5)
    c = ListNode(6)
    d = ListNode(9)
    head.next = b
    b.next = c
    c.next = d


    x = Solution()
    head2 = x.oddEvenList(head)
    head2.print_all()
