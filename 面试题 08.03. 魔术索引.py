class Solution:
    def findMagicIndex(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i

        return -1


if __name__ == '__main__':
    x = Solution()
    print(x.findMagicIndex([0, 2, 3, 4, 5]))






