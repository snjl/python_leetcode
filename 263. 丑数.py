class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 10 == 0:
            num /= 10
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        if num == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    x = Solution()
    print(x.isUgly(11))