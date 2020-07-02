class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        # 统计0的数量
        zero_num = len([i for i in nums if i == 0])
        nums = [i for i in nums if i != 0]
        # 后一个值和前一个值差值大于1，则需要差值-1
        m = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return False
            if nums[i + 1] - nums[i] == 1:
                continue
            else:
                m += (nums[i + 1] - nums[i] - 1)
        if m <= zero_num:
            return True
        else:
            return False

if __name__ == '__main__':
    x = Solution()
    print(x.isStraight([0, 0, 1, 3, 6]))
