class Solution:
    def removeElement(self, nums, val: int) -> int:
        cursor = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if cursor == i:
                    cursor += 1
                else:
                    nums[cursor] = nums[i]
                    cursor += 1
        return cursor




if __name__ == '__main__':
    x = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    cursor = 0
    for i in range(len(nums)):
        if nums[i] != val:
            if cursor == i:
                cursor += 1
            else:
                nums[cursor] = nums[i]
                cursor += 1

    print(cursor)
    print(nums)