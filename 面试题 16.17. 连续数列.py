class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sub = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            max_sub = max(max_sub, nums[i])

        return max_sub


if __name__ == '__main__':
    x = Solution()
    print(x.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
