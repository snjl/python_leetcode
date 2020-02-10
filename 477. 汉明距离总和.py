class Solution:
    def totalHammingDistance(self, nums) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        bin_nums = [bin(num)[2:] for num in nums]
        max_len = max([len(i) for i in bin_nums])
        # 补足数字小的二进制前面部分的0
        bin_nums = ['0' * (max_len - len(i)) + i for i in bin_nums]
        sum = 0
        for i in range(max_len):
            zero_count = [x[i] for x in bin_nums].count('0')
            sum += zero_count * (nums_len - zero_count)
        return sum



if __name__ == '__main__':
    x = Solution()
    print(x[2,14,4])

