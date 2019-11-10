import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)

        for i in range(len(s)):
            if s[i] in d.keys() and d[s[i]] == 1:
                return i

        return -1


if __name__ == '__main__':
    x = Solution()
    s = 'loveleetcode'
    print(x.firstUniqChar(s))

