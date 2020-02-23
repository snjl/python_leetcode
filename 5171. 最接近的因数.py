class Solution:
    def closestDivisors(self, num: int):
        cursor = int(num ** 0.5)
        left = cursor + 1
        right = cursor

        while True:
            result = left * right
            if result == num + 1 or result == num + 2:

                return [left, right]

            elif result > num + 1:
                left -= 1
            elif result < num + 1:
                right += 1


if __name__ == '__main__':
    x = Solution()
    # print(x.closestDivisors(999))
    print(x.closestDivisors(797442477))
