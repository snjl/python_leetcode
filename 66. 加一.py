class Solution:
    def plusOne(self, digits):
        new_digits = [0, ]
        new_digits.extend(digits)
        new_digits = new_digits[::-1]
        flag = 1
        for i in range(len(new_digits)):
            val = new_digits[i] + flag
            if val >= 10:
                val -= 10
                flag = 1
                new_digits[i] = val
            else:
                flag = 0
                new_digits[i] = val
        new_digits = new_digits[::-1]
        if new_digits[0] == 0:
            return new_digits[1:]
        else:
            return new_digits



if __name__ == '__main__':
    x = Solution()
    digits = [9,9,9]

    print(x.plusOne(digits))