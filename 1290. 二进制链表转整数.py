# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode):
        l = list()
        while head is not None:
            l.append(head.val)
            head = head.next

        length = len(l) - 1
        s = 0
        for i in l:
            s += i * (2 ** length)
            length -= 1

        return s



        pass


