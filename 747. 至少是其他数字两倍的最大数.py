class Solution:
    def dominantIndex2(self, nums) -> int:
        max_num = max(nums)
        max_i = nums.index(max_num)
        for i in range(len(nums)):
            if max_i == i:
                continue
            if max_num - 2 * nums[i] < 0:
                return -1

        return max_i

    def dominantIndex(self, nums) -> int:
        if len(nums) == 1:
            return 0

        max_i = nums.index(max(nums))
        nums.sort(reverse=True)
        if nums[0] >= nums[1] * 2:
            return max_i
        else:
            return -1


if __name__ == '__main__':
    x = Solution()

    nums = [3, 6, 1, 0]
    nums = [0, 0, 3, 2]
    # nums = [0,0,0,1]
    print(x.dominantIndex(nums))
