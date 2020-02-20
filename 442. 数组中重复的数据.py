class Solution:
    def findDuplicates(self, nums):
        result = list()


        for i in range(len(nums)):
            # nums[i]为x，则x-1位置为负数表示已经存在过，存入result中
            flag = abs(nums[i])
            if nums[flag - 1] > 0:
                nums[flag - 1] = - nums[flag - 1]
            else:
                result.append(flag )

        return result





if __name__ == '__main__':
    x = Solution()
    l= [4,3,2,7,8,2,3,1]
    print(x.findDuplicates(l))
