class Solution:
    def moveZeroes2(self, nums):
        real_nums = list()

        for i in nums:
            if i != 0:
                real_nums.append(i)

        for i in range(len(nums)):
            if i < len(real_nums):
                nums[i] = real_nums[i]
            else:
                nums[i] = 0
        print(nums)

    def moveZeroes(self,nums):
        # 从0开始走，i遇到不为0的数时才在cursor指针处写入数据，并且增加cursor的值
        cursor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # 如果cursor和i不是同一个位置，说明i之前出现过0
                if cursor != i:
                    nums[cursor] = nums[i]
                cursor += 1

        for i in range(cursor, len(nums)):
            nums[i] = 0

        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]

    # 从0开始走，i遇到不为0的数时才在cursor指针处写入数据，并且增加cursor的值
    cursor = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            # 如果cursor和i不是同一个位置，说明i之前出现过0
            if cursor != i:
                nums[cursor] = nums[i]
            cursor += 1

    for i in range(cursor,len(nums)):
        nums[i] = 0

    print(nums)



