class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义用于存放栈顶的队列（q1）和其他元素的队列（q2）
        import queue as q
        self.q1 = q.Queue()
        self.q2 = q.Queue()
        self.top_num = None
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)
        self.top_num = x
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 将先入队的元素放入q2，在取出q1的最后一个数。
        while self.q1.qsize() > 1:
            self.top_num = self.q1.get()
            self.q2.put(self.top_num)
        res = self.q1.get()
        # 交换q1和q2用于下一次操作
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        # pop后得到top，但要将top重新放入q1
        return self.top_num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty() and self.q2.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
obj.push(1)

param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)