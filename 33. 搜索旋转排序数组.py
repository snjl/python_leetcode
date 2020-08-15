class Solution:
    # def search(self, nums, target: int) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             return mid
    #         # 左半段是有序的
    #         if nums[left] <= nums[mid]:
    #             # target在这段里
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         # 右半段是有序的
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #
    #     return -1

    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # [left, mid] 连续递增
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # [mid, right]连续递增
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    x = Solution()
    nums = [5, 1, 2, 3, 4]

    target = 1
    print(x.search(nums, target))
