class Solution:
    def isPowerOfFour2(self, num: int) -> bool:

        if num % 4 == 0 and num / 4 != 1:
            return self.isPowerOfFour2(int(num / 4))
        elif num / 4 == 1:
            return True
        else:
            return False

    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4

        if num == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    x = Solution()
    a = x.isPowerOfFour(0)
    print(a)
