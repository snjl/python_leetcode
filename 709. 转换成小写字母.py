class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ''
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                new_s += chr(ord(s[i]) + 32)
            else:
                new_s += s[i]
        return new_s

        pass


if __name__ == '__main__':
    x = Solution()

    s = "LOVELY"

    print(x.toLowerCase(s))
