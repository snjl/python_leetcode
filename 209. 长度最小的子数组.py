

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        min_l = len(nums) + 1
        left = 0
        sum_all = 0
        # 右指针未出界，则继续循环
        for i in range(len(nums)):
            sum_all += nums[i]

            while sum_all >= s:
                min_l = min(min_l, i - left + 1)
                sum_all -= nums[left]
                left += 1

        if min_l <= len(nums):
            return min_l
        else:
            return 0


if __name__ == '__main__':
    x = Solution()

    s = 7
    nums = [2, 3, 1, 2, 4, 3]

    # s = 11
    # nums = [1, 2, 3, 4, 5]
    print(x.minSubArrayLen(s, nums))
