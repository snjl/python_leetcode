class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # while n % 3 == 0:
        #     n = n / 3
        # if n == 1:
        #     return True
        # else:
        #     return False
        if n <= 0:
            return False
        return 1162261467 % n == 0

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(243))