class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0
        max_length = 0
        dp = [1 for _ in nums]
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_length = max(max_length, dp[i])
        return max_length


if __name__ == '__main__':
    x = Solution()

    # print(x.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(x.lengthOfLIS([]))
    print(x.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
