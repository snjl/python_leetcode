class Solution:
    def missingNumber(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return -1