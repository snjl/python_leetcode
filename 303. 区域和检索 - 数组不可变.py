class NumArray:
    # 由于反复计算，超时
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for k in range(i,j+1):
            sum += self.nums[k]
        return sum


class NumArray2:
    def __init__(self,nums):
        self.add_nums = [0,]
        for i in range(len(nums)):
            self.add_nums.append(nums[i] + self.add_nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.add_nums[j+1] - self.add_nums[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    # nums = [1,2,3,4,5]
    x = NumArray2(nums)