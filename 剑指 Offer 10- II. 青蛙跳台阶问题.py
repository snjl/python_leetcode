class Solution:
    def numWays(self, n: int) -> int:
        if n== 0:
            return 1
        if n == 1:
            return 1

        l = [0 for _ in range(n + 1)]
        l[0] = 1
        l[1] = 1
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[-1] % 1000000007