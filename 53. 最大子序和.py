class Solution:
    def maxSubArray(self, nums) -> int:
        l = [0 for _ in range(len(nums))]
        l[0] = nums[0]
        for i in range(1, len(nums)):
            pre_max = l[i - 1]
            l[i] = max(pre_max + nums[i], nums[i])
        return max(l)



if __name__ == '__main__':
    x = Solution()

    print(x.maxSubArray([1, 2, -1, 5, 1]))
