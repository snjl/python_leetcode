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

        p = head
        if p is None:
            return p
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

    # 递归版本
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if(head==None or head.next==None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


if __name__ == '__main__':
    x = Solution()

    head = ListNode(4)
    b = ListNode(5)
    c = ListNode(6)
    d = ListNode(9)
    head.next = b
    # b.next = c
    # c.next = d

