class Solution:
    def minMoves(self, nums) -> int:
        m = min(nums)
        num = 0
        for i in nums:
            num +=(i - m)
        return num

