class Solution:
    def isUnique(self, astr: str) -> bool:
        m = set()
        for i in astr:
            if i in m:
                return False
            else:
                m.add(i)
        return True


if __name__ == '__main__':
    x = Solution()
    print(x.isUnique('abca'))
