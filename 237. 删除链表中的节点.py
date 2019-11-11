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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


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

