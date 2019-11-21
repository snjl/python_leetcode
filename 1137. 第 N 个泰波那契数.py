class Solution:
    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==1 or n == 2:
            return 1
        else:
            return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev_3 = 0
        prev_2 = 1
        prev_1 = 1
        sum = 0

        for i in range(n-2):
            sum = prev_1+prev_2+prev_3
            prev_3 = prev_2
            prev_2 = prev_1
            prev_1 = sum
        return sum

if __name__ == '__main__':
    x = Solution()
    print(x.tribonacci(23))
