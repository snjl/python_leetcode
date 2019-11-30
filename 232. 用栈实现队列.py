class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.l.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.l) > 0:

            front = self.l[0]
            self.l = self.l[1:]
            return front

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.l) > 0:

            front = self.l[0]
            return front
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.l) == 0:
            return True
        return False


class MyQueue2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.instack) == 0 and len(self.outstack) == 0

if __name__ == '__main__':
    x = 5
    obj = MyQueue()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()