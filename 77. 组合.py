class Solution:
    def combine(self, n: int, k: int):
        results = list()


        def dfs(start, nums):
            if len(nums) == k:
                results.append(nums[:])
                return

            for i in range(start, n+1):
                nums.append(i)
                dfs(i + 1, nums)
                nums.pop()

        dfs(1, [])
        return results



if __name__ == '__main__':
    x = Solution()
    print(x.combine(4, 2))
