class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.LinkList = list()

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < len(self.LinkList):
            return self.LinkList[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.LinkList.insert(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.LinkList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.LinkList.insert(0, val)
            return
        self.LinkList.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0<=index<=len(self.LinkList) -1:
           self.LinkList.pop(index)



# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()
linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1,2)  #链表变为1-> 2-> 3
# linkedList.get(1)         #返回2
# linkedList.deleteAtIndex(1) #现在链表是1-> 3
# linkedList.get(1)       #返回3
