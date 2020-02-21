class Solution:
    def search(self, nums, target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # print(left,mid,right)
            if nums[mid] == target:
                return True
            # 左半段是有序的
            if nums[left] < nums[mid]:
                # target在这段里
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半段是有序的
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1

        return False


if __name__ == '__main__':
    x = Solution()
    nums = [1,3,1,1,1]

    target = 3
    print(x.search(nums, target))
