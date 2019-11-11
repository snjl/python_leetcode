class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        pow_x = pow(3, x)
        while pow_x <= n:
            if pow_x == n:
                return True
            else:
                x += 1
                pow_x = pow(3, x)
        return False

    def isPowerOfThree2(self, n: int) -> bool:

        if n <= 0:
            return False
        return 1162261467 % n == 0
if __name__ == '__main__':
    x = Solution()
    n = 792

    print(x.isPowerOfThree(n))
