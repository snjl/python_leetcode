class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        nums1 = nums[1:]
        nums2 = nums[:-1]

        def sub_rob(nums) -> int:
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
        max1 = sub_rob(nums1)
        max2 = sub_rob(nums2)

        return max(max1,max2)


if __name__ == '__main__':
    x = Solution()
    print(x.rob([2, 3, 2]))
