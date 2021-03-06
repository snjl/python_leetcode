class Solution:
    def twoSum2(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                # 如果目标值减去该num的值在d的键值对里，则返回d[num]=i中的i，如果不存在，则使d[num]=i
                return d[target - num], i
            d[num] = i

    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                return [d.get(nums[i]), i]
            d[target - nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    a = s.twoSum([2, 5, 7, 9], 9)
    print(a)
