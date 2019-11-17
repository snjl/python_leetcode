class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        while sum != target:
            if sum > target:
                right -= 1
                sum = numbers[left] + numbers[right]
            else:
                left += 1
                sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]



if __name__ == '__main__':
    x = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
