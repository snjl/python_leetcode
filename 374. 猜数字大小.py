def guess(num: int) -> int:


    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n + 1
        while left <= right:
            mid = int((left + right) / 2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1

            else:
                left = mid + 1

        return -1
