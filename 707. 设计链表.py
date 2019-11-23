class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        h = self.head
        for i in range(index):
            if h.next:
                h = h.next
            else:
                return -1
        return h.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head == None:
            self.head = Node(val)
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        h = self.head
        while h.next:
            h = h.next
        h.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        # 如果index<=0，则插入头节点
        if index<=0:
            self.addAtHead(val)
            return
        # 否则进行插入
        h = self.head
        for i in range(index-1):
            if h.next:
                h = h.next
            # 如果链表已经到末尾，还未结束，说明超出链表长度，不插入
            else:
                return
        # 如果链表还有下一个节点，则是正常插入
        if h.next:
            n = Node(val)
            n.next = h.next
            h.next = n
        # 如果没有下一个节点，直接插入即可
        else:
            h.next = Node(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return

        h = self.head

        for i in range(index-1):
            if h.next:
                h = h.next
            else:
                return
        # 如果还有next
        if h.next:
            h.next = h.next.next
        # 如果没有next
        else:
            return




# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1,2)  #链表变为1-> 2-> 3
linkedList.get(1)         #返回2
linkedList.deleteAtIndex(1) #现在链表是1-> 3
linkedList.get(1)       #返回3

