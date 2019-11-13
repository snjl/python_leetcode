class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = max(len(a), len(b)) + 1
        s = ''
        flag = 0
        for i in range(x):
            if len(a) > i:
                a_val = a[-i - 1]
            else:
                a_val = 0
            if len(b) > i:
                b_val = b[-i - 1]
            else:
                b_val = 0
            val = int(flag) + int(a_val) + int(b_val)
            if val >= 2:
                flag = 1
                s = str(val - 2) + s
            else:
                flag = 0
                s = str(val) + s
        if s[0] == '0':
            return s[1:]
        return s




if __name__ == '__main__':
    x = Solution()


