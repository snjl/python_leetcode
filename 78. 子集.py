class Solution:
    def subsets(self, nums):

        l = list()

        def dfs(start, sub_nums):
            l.append(sub_nums[:])
            for i in range(start, len(nums)):
                sub_nums.append(nums[i])
                dfs(i + 1, sub_nums)
                sub_nums.pop()

        dfs(0, [])
        return l




if __name__ == '__main__':
    x = Solution()

    print(x.subsets([1, 2, 3]))
