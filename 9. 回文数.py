class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        len_s = len(s)
        l = int(len_s / 2)
        for i in range(l):
            if s[i] == s[len_s - i - 1]:
                continue
            else:
                return False
        return True

# 直接判断翻转过来的字符串是不是一样
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            result = False
        else:
            strx = str(x)
            result = strx == strx[::-1]
        return result


if __name__ == '__main__':
    x = 122211

    s = Solution()
    s.isPalindrome(x)