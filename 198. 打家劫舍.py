class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        for i in range(2, len(nums)):
            if i >= 3:
                nums[i] += max(nums[i - 2], nums[i - 3])
            else:
                nums[i] += nums[i - 2]
        return max(nums)


if __name__ == '__main__':
    x = Solution()
    print(x.rob([2, 1, 1, 2]))
