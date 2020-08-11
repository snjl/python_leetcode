class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if len(cost) <= 2:
            return min(cost)
        # 最后补充个0，表示最后需要0体力到达
        cost.append(0)
        l = [0 for _ in range(len(cost))]
        l[0] = cost[0]
        l[1] = cost[1]
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2] + cost[i], cost[i - 1] + cost[i])

        return cost[-1]


if __name__ == '__main__':
    x = Solution()
    print(x.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

