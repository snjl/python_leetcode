class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        l = [0 for _ in range(n + 1)]
        l[0] = 1
        l[1] = 1
        l[2] = 2
        for i in range(3, n + 1):
            l[i] = (l[i-3] + l[i-2] + l[i-1]) % 1000000007
        return l[-1]



if __name__ == '__main__':
    x = Solution()
    print(x.waysToStep(2))


