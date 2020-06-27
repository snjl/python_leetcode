# Definition for singly-linked list.
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
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = head

        q = head.next
        # 表示只有一个节点
        if q is None:
            return p
        # 将第一个节点置空
        p.next = None
        # 如果q还有下一个节点，则不断交换，q永远在p前面
        while q.next:
            # 令m为q，q往前走，m指向p，p令为m
            m = q
            q = q.next
            m.next = p
            p = m
        q.next = p
        return q



if __name__ == '__main__':
    head = [4, 5, 1, 9]

    node = 5

    a = ListNode(4)
    b = ListNode(5)
    c =ListNode(6)
    d = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    a.print_all()
    x = Solution()
    x.reverseList(a)
    d.print_all()


