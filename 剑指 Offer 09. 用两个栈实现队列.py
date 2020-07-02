class CQueue:

    def __init__(self):
        self.l1 = list()
        self.l2 = list()
        pass

    def appendTail(self, value: int) -> None:
        self.l1.append(value)


    def deleteHead(self) -> int:
        if len(self.l1) == 0 and len(self.l2) == 0:
            return -1
        if len(self.l2) > 0:
            return self.l2.pop()

        else:
            while len(self.l1) > 0:
                self.l2.append(self.l1.pop())
            return self.l2.pop()




if __name__ == '__main__':
    x = CQueue()
    x.appendTail(3)
    x.deleteHead()
    x.deleteHead()
