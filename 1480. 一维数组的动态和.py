class Solution:
    def runningSum(self, nums):
        l = [0 for _ in range(len(nums))]
        l[0] = nums[0]
        for i in range(1, len(nums)):
            l[i] = l[i - 1] + nums[i]
        return l


if __name__ == '__main__':
    x = Solution()

    print(x.runningSum([1, 2, 3, 4, 5]))
