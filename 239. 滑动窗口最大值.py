class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = list()
        for i in range(0, len(nums) - k + 1):
            max_nums = nums[i:i + k]
            # print(max_nums)
            l.append(max(max_nums))

        return l

        pass


if __name__ == '__main__':
    x = Solution()
    print(x.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
