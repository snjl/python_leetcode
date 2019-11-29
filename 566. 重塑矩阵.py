class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        old_r = len(nums)
        old_c = len(nums[0])
        if r * c != old_r * old_c:
            return nums
        new_i = 0
        new_j = 0
        new_nums = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(old_r):
            for j in range(old_c):
                new_nums[new_i][new_j] = nums[i][j]
                if new_j == c - 1:
                    new_i += 1
                    new_j = 0
                else:
                    new_j += 1
        return new_nums

if __name__ == '__main__':
    x = Solution()

    nums = [[1, 2],
     [3, 4]]

    print(x.matrixReshape(nums,4,1))
