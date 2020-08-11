class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        s_point = 0
        for i in range(len_t):
            if s_point == len_s:
                return True
            if t[i] == s[s_point]:
                s_point += 1
        if s_point == len_s:
            return True
        return False


if __name__ == '__main__':
    x = Solution()
    s = "axc"
    t = "ahbgdc"
    print(x.isSubsequence(s, t))
