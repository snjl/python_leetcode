class Solution:
    def findMin(self, nums) -> int:

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[mid + 1]:
                return nums[mid + 1]
            # 说明后半部分有序
            if nums[mid] < nums[right]:
                right = mid
            # 前半部分有序
            else:
                left = mid + 1

        return nums[left]


if __name__ == '__main__':
    x = Solution()
    l  =[0,1,2]
    print(x.findMin(l))



