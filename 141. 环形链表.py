class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + ("->" if self.next is not None else "")

    # def __repr__(self):
    #     return str(self.val)

    def print_all(self):
        a = self
        while a:
            if a.next:
                print(a, end='')
            else:
                print(a)
            a = a.next

class Solution:
    # 哈希表方法，把经过的节点都存入哈希表中，再遇到即有环
    def hasCycle3(self, head: ListNode) -> bool:
        l = list()
        while head:
            if head not in l:
                l.append(head)
                head = head.next
            else:
                return True
        return False

    # 内置一个特殊字符，每到一个位置就进行标记，如果发现返回到了这个标记即有环
    def hasCycle2(self, head: ListNode) -> bool:
        while head:
            if head.val != 'cctvttv':
                head.val = 'cctvttv'
                head = head.next
            else:
                return True
        return False

    # 快慢指针，快指针走两步，慢指针走一步，快指针追上慢指针即是有环
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False





if __name__ == '__main__':
    x = Solution()

    head = ListNode(4)
    b = ListNode(5)
    c = ListNode(6)
    d = ListNode(9)
    head.next = b
    b.next = c
    c.next = head

    # head.print_all()
    print(x.hasCycle(head))



