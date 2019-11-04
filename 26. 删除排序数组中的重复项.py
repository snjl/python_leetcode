class Solution:
    def removeDuplicates(self, nums):
        cursor = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[cursor]:
                pass
            else:
                cursor += 1
                nums[cursor] = nums[i]

        return cursor + 1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3, 4, 5, 5, 6]))
