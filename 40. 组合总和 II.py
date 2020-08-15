class Solution:
    def combinationSum2(self, candidates, target: int):
        results = list()
        candidates.sort()
        m = dict()
        for i in candidates:
            m[i] = m.get(i,0) + 1

        self.dfs(0, [], 0, results, target, candidates,m)
        return results

    def dfs(self, start, nums, now_all, results, target, candidates,m):
        if now_all == target:
            if nums not in results:
                results.append(nums[:])
            return

        for i in range(start, len(candidates)):
            nums.append(candidates[i])
            now_all = sum(nums)
            if now_all > target:
                return

            self.dfs(i + 1, nums.copy(), now_all, results, target, candidates,m)
            nums.pop()


if __name__ == '__main__':
    x = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(x.combinationSum2(candidates, target))
