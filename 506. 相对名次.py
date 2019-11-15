class Solution:
    def findRelativeRanks(self, nums):
        # 用于存储排名
        nums_str = nums.copy()
        d = {}
        # 将每个元素的位置存储到dict中
        for i in range(len(nums)):
            d[nums[i]] = i

        nums.sort(reverse=True)

        if len(nums) > 0:
            nums_str[d[nums[0]]] = "Gold Medal"
        if len(nums) > 1:
            nums_str[d[nums[1]]] = "Silver Medal"
        if len(nums) > 2:
            nums_str[d[nums[2]]] = "Bronze Medal"
        if len(nums) > 3:
            num = 4
            for i in nums[3:]:
                nums_str[d[i]] = str(num)
                num += 1

        return nums_str

if __name__ == '__main__':
    x = Solution()
    nums = [1, ]
    print(x.findRelativeRanks(nums))
