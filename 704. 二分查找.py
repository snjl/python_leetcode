class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((right + left) / 2)
            # print(left, mid, right)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    x = Solution()
    nums = [-1, 0, 3, 5, 9, 12]

    target = 9
    print(x.search(nums, target))
