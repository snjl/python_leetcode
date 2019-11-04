class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]

    def __len__(self):
        return self.stack.__len__()
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'{': '}', '(': ')', '[': ']'}
        right_list = list()
        for i in s:
            # 如果是d的key，即左符号，则把对应的右符号存入right_list
            if d.get(i):
                right_list.append(d.get(i))
            # 如果不是d的key，即为右符号，判断是否为对应的右符号，如果不是则返回False
            elif len(right_list) >= 1 and i == right_list[-1]:
                right_list = right_list[:-1]
            else:
                return False
        # 如果匹配到最后一个字符串，valid_list还有存货，则匹配失败
        if len(right_list) is 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        d = {'{': '}', '(': ')', '[': ']'}
        stack = Stack()
        for i in s:
            # 如果是d的key，即左符号，则把对应的右符号存入right_list
            if d.get(i):
                stack.push(d.get(i))
            # 如果不是d的key，即为右符号，判断是否为对应的右符号，如果不是则返回False
            elif len(stack) >= 1 and i == stack.pop():
                pass
            else:
                return False
        # 如果匹配到最后一个字符串，valid_list还有存货，则匹配失败
        if len(stack) is 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    a = s.isValid2("{[[}")
    # a = s.isValid("[()]")
    print(a)
