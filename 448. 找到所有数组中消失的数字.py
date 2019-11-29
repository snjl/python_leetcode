class Solution:
    def findDisappearedNumbers(self,nums):
        m = dict()
        for i in range(len(nums)):
            m[i+1] = 0
        for i in nums:
            m[i]+=1
        l = list()
        for k,v in m.items():
            if v == 0:
                l.append(k)

        return l

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
        # 举个例子：
        # 原始数组：[4,3,2,7,8,2,3,1]
        # 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        # 结论：[8,2] 分别对应的index为[5,6]（消失的数字）
        for num in nums:
            index = abs(num) - 1
            # 始终保持nums[index]为负数
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
