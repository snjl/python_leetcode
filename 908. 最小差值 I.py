class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        m = min(A)
        n = max(A)
        if n - m - 2 * K > 0:
            return n - m - 2 * K
        else:
            return 0


if __name__ == '__main__':
    x = Solution()

    A = [0,10]
    K = 2
    print(x.smallestRangeI(A, K))

