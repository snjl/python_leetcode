class Solution:
    def combinationSum(self, candidates, target: int):
        results = list()
        candidates.sort()

        self.dfs(0, [], 0, results, target, candidates)
        return results

    def dfs(self, start, nums, now_all, results, target,candidates):
        if now_all == target:
            results.append(nums[:])
            return

        for i in range(start, len(candidates)):
            nums.append(candidates[i])
            now_all = sum(nums)
            if now_all > target:
                return

            self.dfs(i, nums.copy(), now_all, results, target,candidates)
            nums.pop()


if __name__ == '__main__':
    x = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(x.combinationSum(candidates, target))
