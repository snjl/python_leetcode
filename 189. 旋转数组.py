class Solution:
    def rotate2(self, nums, k) -> None:
        l = len(nums)
        for i in range(k):
            # x存储被右移的数字
            x = nums[-1]
            # 倒序把数字右移
            for i in range(l-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = x


    def rotate(self, nums, k) -> None:
        k %= len(nums)
        nums.reverse()
        # print(nums)
        nums[:k] = nums[:k][::-1]
        # print(nums)
        nums[k:] = nums[k:][::-1]
        # print(nums)
        return nums


if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5,6,7]
    w = s.rotate(a, 3)
