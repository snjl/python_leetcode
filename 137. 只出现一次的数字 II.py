class Solution:
    def singleNumber(self, nums) -> int:
        x,y = 0,0
        for i in nums:
            x = (i^x) & ~y
            y = (i^y) & ~x
        return x
