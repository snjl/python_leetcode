class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 长度长的作为被乘数
        if len(num1) < len(num2):
            num2, num1 = num1, num2

        num2 = num2[::-1]
        s = '0'
        for i in range(len(num2)):
            for j in range(int(num2[i])):
                s = self.addStrings(s, num1 + '0' * i)
                # print(s)
        return s

    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        s = ''
        # 进位
        last = 0
        for i in range(length):
            if i < len(num1):
                n1 = num1[i]
            else:
                n1 = 0
            if i < len(num2):
                n2 = num2[i]
            else:
                n2 = 0
            n = int(n1) + int(n2) + int(last)
            if n >= 10:
                n -= 10
                last = 1
            else:
                last = 0

            s += str(n)
        if last == 1:
            s += str(last)
        return s[::-1]


if __name__ == '__main__':
    x = Solution()
    num1 = "123"
    num2 = "456"
    print(x.multiply(num1, num2))


