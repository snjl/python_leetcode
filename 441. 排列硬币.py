class Solution:
    def arrangeCoins(self, n: int) -> int:
        g =1
        while g*(g+1) /2 <= n:
            g += 1
        return g - 1


if __name__ == '__main__':
    x = Solution()
    print(x.arrangeCoins(5))