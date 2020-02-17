class Solution:
    def maxSubArray(self, nums) -> int:


        return self.maxSub(nums,0,len(nums))

    def maxSub(self,nums,i,j):



        return 0