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
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2

        sum = ListNode(-1)
        sum_head = sum
        flag = 0
        while p and q:
            val = p.val + q.val + flag
            # 计算第i次计算中，p，q和flag的value和，如果超过10，则进位
            if val >= 10:
                flag = 1
                val -= 10
            else:
                flag = 0
            sum.next = ListNode(val)
            sum = sum.next
            p = p.next
            q = q.next

        # 如果p不为空，则用p，否则用q
        has_next_node = p if p is not None else q

        # 如果还有进位没有处理
        if flag == 1:
            # 节点均不存在后续存在后续
            if has_next_node is None:
                sum.next = ListNode(flag)
            # 节点存在后续，则继续计算
            else:
                while has_next_node:
                    val = has_next_node.val + flag
                    if val >= 10:
                        flag = 1
                        val -= 10
                    else:
                        flag = 0
                    sum.next = ListNode(val)
                    sum = sum.next
                    has_next_node = has_next_node.next
        else:
            sum.next = has_next_node
        if flag == 1:
            sum.next = ListNode(flag)

        return sum_head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode(-1)
        sum_head = sum
        # 判断是否进位
        flag = 0
        # l1或l2中还有后续节点，或进位为1则继续算
        while l1 is not None or l2 is not None or flag:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            val = l1.val + l2.val + flag
            # 计算下一个进位
            if val >=10:
                val -= 10
                flag = 1
            else:
                flag = 0
            sum.next = ListNode(val)

            l1 = l1.next
            l2 = l2.next
            sum = sum.next
        return sum_head.next


if __name__ == '__main__':
    x = Solution()

    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(3)
    l5 = ListNode(6)
    l6 = ListNode(4)

    l4.next = l5
    l5.next = l6

    w = x.addTwoNumbers(l1, l4)
    w.print_all()

    lx = ListNode(5)
    ly = ListNode(5)
    w = x.addTwoNumbers(lx, ly)
    w.print_all()

    lx = ListNode(1)
    lx.next = ListNode(8)
    ly = ListNode(0)
    w = x.addTwoNumbers(lx, ly)
    w.print_all()


    lx = ListNode(9)
    lx.next = ListNode(9)

    ly = ListNode(1)
    w = x.addTwoNumbers(lx, ly)
    w.print_all()
