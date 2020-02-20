class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) <= 3:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid] and nums[right] < nums[mid]:
                left1 = left
                right1 = mid
                while left1 <= right1:
                    mid1 = int((left1 + right1) / 2)

                    if nums[mid1] < target:
                        left1 = mid1 + 1
                    elif nums[mid1] > target:
                        right1 = mid1 - 1
                    else:
                        return mid1

                left2 = mid + 1
                right2 = len(nums) - 1
                while left2 <= right2:
                    mid2 = int((left2 + right2) / 2)
                    if nums[mid2] < target:
                        left2 = mid2 + 1
                    elif nums[mid2] > target:
                        right2 = mid2 - 1
                    else:
                        return mid2
                break

            elif nums[left] < nums[mid] < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    x = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    target = 1
    print(x.search(nums, target))
