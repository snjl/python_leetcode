class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        real_s = ''
        s = s.lower()
        for i in s:
            if str.islower(i) or str.isalnum(i):
                real_s += i

        return real_s == real_s[::-1]


if __name__ == '__main__':
    w = Solution()
    s = 'A man, a plan, a canal: Panama'

    print()


