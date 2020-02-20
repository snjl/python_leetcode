class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = int(x / 2)
        while left <= right:
            mid = int((left + right) / 2)
            num = mid * mid
            if num < x:
                left = mid + 1
            elif num > x:
                right = mid - 1
            else:
                return mid

        return right


if __name__ == '__main__':
    x = Solution()
    print(x.mySqrt(4))
