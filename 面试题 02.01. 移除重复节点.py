# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        exists = list()
        h = ListNode(-1)
        # 构建头节点
        h.next = head
        head = h


        while h.next is not None:
            next = h.next
            if next.val in exists:
                h.next = next.next
                # h = h.next
                # print(h.val)

            else:
                exists.append(next.val)
                h = h.next
        return head.next


if __name__ == '__main__':
    x = Solution()

    # x.removeDuplicateNodes()

