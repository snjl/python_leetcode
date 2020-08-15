class Solution:
    res = list()

    def permute(self, nums):

        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, now_res):
        if len(now_res) == len(nums):
            # print(now_res)
            self.res.append(now_res[:])
            return
        for i in nums:
            if i not in now_res:
                now_res.append(i)
                self.dfs(nums, now_res)
                now_res.pop()


if __name__ == '__main__':
    x = Solution()
    # nums = [1, 2, 3, 5, 6]
    nums = [1, ]

    print(x.permute(nums))
