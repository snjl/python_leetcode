class Solution:
    def findMin(self, nums) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]


if __name__ == '__main__':
    x = Solution()
    nums = [2, 2, 2, 0, 1]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [1, 2, 3]
    # nums = [2, 2]
    print(x.findMin(nums))
