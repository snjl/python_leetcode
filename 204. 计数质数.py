import math

class Solution:
    def countPrimes(self, n: int) -> int:
        # 由于是小于n，不是小于等于，所以这里-1表示小于等于n，效果相同
        n -= 1
        if n <= 1:
            return 0

        # 不用第0位，可以计算到l[n]
        l = [True for _ in range(0, n + 1)]

        for i in range(2, int(math.sqrt(n) + 1)):
            if l[i] is True:
                for j in range(2, int(n / i) + 1):
                    l[j * i] = False
        l[0] = False
        l[1] = False
        return l.count(True)


if __name__ == '__main__':
    x = Solution()
    print(x.countPrimes(10))
