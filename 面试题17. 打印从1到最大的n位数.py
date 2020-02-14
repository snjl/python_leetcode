class Solution:
    def printNumbers(self, n: int):
        x = 0
        for i in range(1,n+1):
            x = 10 * x + 9
        return [i for i in range(1,x+1)]


if __name__ == '__main__':
    x = Solution()
    print(x.printNumbers(2))
