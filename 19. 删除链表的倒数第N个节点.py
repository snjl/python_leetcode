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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = list()

        p = head
        while p:
            node_list.append(p)
            p = p.next

        # 如果节点数量为1
        if len(node_list) == 1:
            return None
        # 如果要删除的是最后一个节点，则上一个节点指向None
        if n == 1:
            node_list[-2].next = None
        # 如果要删除的是第一个节点
        if len(node_list) == n:
            head = head.next
        else:
            p, q = node_list[-n - 1], node_list[-n]
            p.next = q.next


        return head


if __name__ == '__main__':

    n = 2

    head = ListNode(4)
    # b = ListNode(5)
    # c = ListNode(6)
    # d = ListNode(9)
    # head.next = b
    # b.next = c
    # c.next = d


    x = Solution()
    head2 =  x.removeNthFromEnd(head,1)
    head2.print_all()
