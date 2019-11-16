class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        s = 0
        for i in range(0,len(nums),2):
            s +=min(nums[i],nums[i+1])
        return s
