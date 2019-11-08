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
    # 迭代方法
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # 哨兵节点
        pre_head = ListNode(-1)
        # 用于移动存储的节点
        prev = pre_head
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next
        # 如果l1还有后续（由于l2没有了后续，所以循环会终止），则直接把l1接到最后，否则把l2接到最后
        prev.next = l1 if l1 is not None else l2

        return pre_head.next

    # 递归方法
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(1)
    l5 = ListNode(3)
    l6 = ListNode(4)

    l4.next = l5
    l5.next = l6

    s = Solution()
    s.mergeTwoLists(l1, l4).print_all()
