class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = dict()
        for i in s:
            if i not in m.keys():
                m[i] = 1
            else:
                m[i] += 1
        count = 0

        for k,v in m.items():
            count += int(v/2)
        if count * 2 == len(s):
            return count * 2
        else:
            return count * 2 + 1

if __name__ == '__main__':
     x = Solution()
     print(x.longestPalindrome('abc'))