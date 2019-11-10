class Solution:
    def reverseString2(self, s):
        l = len(s)
        for i in range(int(l / 2)):
            temp = s[i]
            s[i] = s[l - i - 1]
            s[l - i - 1] = temp

    def reverseString(self, s):
        s.reverse()


if __name__ == '__main__':
    s = Solution()

    w = ["h", "e", "l", "l", "o"]

    s.reverseString(w)
    print(w)





