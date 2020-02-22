class Solution:

    def findDuplicate(self, nums) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

    def findDuplicate3(self, nums) -> int:
        # 数组只能读 所以不能排序,不能swap数组下标
        # 时间复杂度小于 O(n^2) 不能暴力
        # 空间复杂度 O(1) 不能额外开辟数组

        ''' 1、暴力不符合题意
        for i in nums:
            count = 0
            for num in nums:
                if num == i:
                    count += 1
            if count > 1:
                return i
        return -1
        '''

        '''2、小于O(n^2) 二分查找
        我们不要考虑数组,只需要考虑 数字都在 1 到 n 之间
        示例 1:
        arr = [1,3,4,2,2] 此时数字在 1 — 5 之间

        mid = (1 + 5) / 2 = 3 arr小于等于的3有4个(1,2,2,3)，1到3中肯定有重复的值
        mid = (1 + 3) / 2 = 2 arr小于等于的2有3个(1,2,2)，1到2中肯定有重复的值
        mid = (1 + 2) / 2 = 1 arr小于等于的1有1个(1)，2到2中肯定有重复的值
        所以重复的数是 2 
        '''
        left = 1
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right
