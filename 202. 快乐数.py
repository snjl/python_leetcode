class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in list(str(n))])
            if n in s:
                return False
            s.add(n)

        return True

if __name__ == '__main__':
    x = Solution()

    n=12

    print(x.isHappy(n))
