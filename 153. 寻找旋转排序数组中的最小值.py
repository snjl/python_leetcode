# class Solution:
#     def findMin(self, nums) -> int:
#
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] >= nums[mid + 1]:
#                 return nums[mid + 1]
#             # 说明后半部分有序
#             if nums[mid] < nums[right]:
#                 right = mid
#             # 前半部分有序
#             else:
#                 left = mid + 1
#
#         return nums[left]


class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1

        return -1

    def findNum(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    x = Solution()
    l = [4, 5, 6, 7, 0, 1, 2]
    l = [1, 2, 3, 4, 5]
    # lis = [2, 4, 5, 12, 14, 23]
    # l = [4, 5, 6, 7, 0, 1, 2]
    # print(x.findNum(lis, 5))

    print(x.findMin(l))
