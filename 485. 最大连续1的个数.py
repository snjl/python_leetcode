class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_num = 0
        one_num = 0
        for i in nums:
            if i == 1:
                one_num += 1
            else:
                if max_num > one_num:
                    pass
                else:
                    max_num = one_num
                one_num = 0
        if one_num > max_num:
            max_num = one_num
        return max_num
