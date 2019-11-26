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
    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return None
        p = head
        q = p.next
        while q:
            if q.val == val:
                q = q.next
                p.next = q
            else:
                p = p.next
                q = q.next

        return head

    # 增加哑结点
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        x = ListNode(-1)
        x.next = head
        p = x
        while head:
            if head.val != val:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return x.next

    def removeElements3(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        # 因为要删除的可能是链表的第一个元素，所以用一个h节点来做处理
        # 最后只要返回h的下一个节点即可
        p.next, h = head, p
        # 注意遍历的条件是p.next不为空
        while p.next:
            # 如果p的下一个节点的值==val
            # P就指向下下一个，这就删掉了指定的节点
            if p.next.val == val:
                p.next = p.next.next
                # 注意这里的continue
                # 因为循环最后还有一个P=p.next，所以要跳过
                continue
            # 不用continue用else的方式也是可以的
            p = p.next
        return h.next


if __name__ == '__main__':
    x = Solution()

    head = ListNode(1)
    b = ListNode(2)
    head.next = b
    c = x.removeElements(head, 1)

    c.print_all()
