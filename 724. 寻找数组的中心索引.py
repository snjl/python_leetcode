class Solution:
    def pivotIndex2(self, nums) -> int:
        # 长度为0或2直接返回-1，因为必定找不到一个中心数，长度为1返回0，因为左右都是0
        if len(nums) == 1:
            return 0
        elif len(nums) == 0 or len(nums) == 2:
            return -1
        right_sum = sum(nums)
        left_sum = 0
        # 先减去最左边一格，以后就可以统一形式
        right_sum -= nums[0]
        # 如果右边和已为0，则返回位置0即可，左边为0，右边也为0
        if right_sum == 0:
            return 0
        for i in range(1, len(nums)):
            # 由于i表示的是中心索引，所以不参与运算，左边sum根据i往右走，每次加nums[i-1]，右边的每次减少nums[i]
            left_sum += nums[i - 1]
            right_sum = right_sum - nums[i]

            if left_sum == right_sum:
                return i
        return -1

    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1




if __name__ == '__main__':
    x = Solution()

    nums = [1, 7, 3, 6, 5, 6]
    nums = []
    nums = [1,2,1]
    # print(x.pivotIndex(nums))



