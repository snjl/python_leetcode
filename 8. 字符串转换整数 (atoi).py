class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = 0
        if len(s) == 0:
            return 0
        # 如果首字符是数字或者负号，则进行处理
        if str.isdigit(s[0]):

            for i in s:
                if str.isdigit(i):

                    num = num * 10 + int(i)
                else:
                    break
            if num >= 2147483647:
                return 2 ** 31 - 1
            return num
        elif s[0] == '+':
            s = s[1:]
            for i in s:
                if str.isdigit(i):

                    num = num * 10 + int(i)
                else:
                    break
            if num >= 2147483647:
                return 2 ** 31 - 1
            return num
        elif s[0] == '-':
            s = s[1:]
            for i in s:
                if str.isdigit(i):

                    num = num * 10 + int(i)
                else:
                    break
            if num >= 2147483648:
                return -2 ** 31
            return -num
        else:
            return 0


if __name__ == '__main__':
    x = Solution()
    s = "-91283472332"
    s = '+1'
    s = "2147483648"

    print(x.myAtoi(s))
