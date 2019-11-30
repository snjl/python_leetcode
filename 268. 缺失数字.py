class Solution:
    # # 含有某一位，就把该位对应的index取负数，如果所有位置都为负数，则缺失n，否则缺失该位置的数值
    # def missingNumber(self, nums) -> int:
    #     n = len(nums)
    #     for i in range(n):
    #         # 如果nums[i]为n，为防止越界而跳过，其他位置均是负数时，说明缺失n
    #         if abs(nums[i]) != n:
    #             # nums[i]表示这个值的index，为了保证每次置为负数不会改变后续的操作，每次调取时使用绝对值
    #             nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
    #     # print(nums)
    #     # 如果所有位置都为负数，则缺失n，否则缺失该位置的数值
    #     for i in range(n):
    #         if nums[i] > 0:
    #             return i
    #     return n

    # 求异或，最后留下的值为缺失值（因为其他都会异或位置，导致会两两对应）
    def missingNumber2(self, nums):
        x = len(nums)
        for i in range(len(nums)):
            x ^= i
            x ^= nums[i]
        return x

    # 数学方法，0-n的和加起来后一个个减去，少的就是缺失的
    def missingNumber3(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == '__main__':
    x = Solution()

    # nums = [9,6,4,2,3,5,7,0,1]
    nums = [2,0]
    print(x.missingNumber2(nums))
    print(x.missingNumber3(nums))
    print(x.missingNumber(nums))
