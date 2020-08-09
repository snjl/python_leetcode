class Solution:
    def makeGood(self, s: str) -> str:
        chars = list()
        for i in range(65, 65+26):
            char = chr(i+32) + chr(i)
            chars.append(char)
            char = chr(i) + chr(i + 32)
            chars.append(char)

        before_len = len(s)
        after_len = 0

        while before_len != after_len:
            before_len = len(s)
            for char in chars:
                s = s.replace(char, '')
            after_len = len(s)
        return s




if __name__ == '__main__':
    x = Solution()
    print(x.makeGood("Pp"))