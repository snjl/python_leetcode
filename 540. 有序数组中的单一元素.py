class Solution:
    # 由题可知，至少有三个数，所以不需要判断数组长度
    def singleNonDuplicate(self, nums) -> int:
        p = list()
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]

        for i in nums:
            if len(p) == 0:
                p.append(i)
            else:
                if i == p[0]:
                    p.pop(0)
                else:
                    return p.pop(0)
        return nums[-1]

    def singleNonDuplicate2(self, nums) -> int:
        if nums[0] != nums[1]:
            return nums[0]
        high = len(nums) - 1
        if nums[high] != nums[high - 1]:
            return nums[high]
        low = 2
        high -= 2
        while True:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid] != nums[mid-1]:  # 和左边不同
                if (mid-low) % 2:  # 左边为奇数个
                    high = mid-1
                else:  # 左边为偶数个
                    low = mid+2
            else:  # 和右边不同
                if (high-mid) % 2:  # 右边为奇数个
                    low = mid+1
                else:  # 右边为偶数个
                    high = mid-2

if __name__ == '__main__':
    x = Solution()
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(x.singleNonDuplicate2(nums))
