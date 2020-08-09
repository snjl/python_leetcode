class Solution:
    def massage(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        nums[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        # print(nums)
        return nums[-1]


if __name__ == '__main__':
    x = Solution()
    print(x.massage([2, 1, 1, 2]))
