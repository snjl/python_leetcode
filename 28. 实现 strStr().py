class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) ==0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                flag = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i + j]:
                        flag = False
                        break
                if flag is True:
                    return i
        return -1






if __name__ == '__main__':
    x = Solution()
    haystack = "hello"
    needle = "o"
    needle_start = 0






