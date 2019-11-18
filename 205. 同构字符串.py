class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = dict()
        for i in range(len(s)):
            if s[i] in d.keys():
                if d[s[i]] != t[i]:
                    return False
            # 如果发现t的值在value中出现了，且对应的不是该key值，则返回false
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        return True


if __name__ == '__main__':
    x = Solution()

    s = "egg"
    t = "add"

    print(x.isIsomorphic(s,t))



