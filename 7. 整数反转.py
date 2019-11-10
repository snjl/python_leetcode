class Solution:
    def reverse(self, x):
        low = -pow(2, 31)
        high = pow(2, 31) - 1

        if low <= x <= high:
            x = str(x)
            if x[0] == '-':
                x = - int(x[1:][::-1])

            else:
                x = int(x[::-1])

            if low <= x <= high:
                return x

        return 0


if __name__ == '__main__':
    s = Solution()

    a = -123

    print(s.reverse(a))
