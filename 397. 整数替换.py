class Solution:
    def integerReplacement(self, n: int) -> int:
        num = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
                num += 1
            else:
                n -= 1
                n /= 2
                num += 2
        return num
