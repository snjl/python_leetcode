class Solution:
    # 递归方法，超时
    def coinChange3(self, coins, amount: int) -> int:
        if amount == 0:
            return 0

        # 最大代价为无限大，如果找到了比无限大小的，即说明可以换零钱
        cost = float('inf')
        # 对每个coin都进行计算，如果全是小于0的，则说明此路不通，并且最后返回cost
        for coin in coins:
            # 如果减去后小于0，说明以这种方式换零钱不对，金额不可达
            if amount - coin < 0:
                continue
            # 计算减去coin后，还需要的硬币数量
            sub_amount = self.coinChange3(coins, amount - coin)
            # 如果发现获得的下层节点得到的是-1，表示已经发生金钱不可达的情况，不再考虑
            if sub_amount == -1:
                continue
            # 求出最小代价
            cost = min(sub_amount + 1, cost)
        # 如果发现金钱不可达，返回-1
        if cost == float('inf'):
            return -1
        else:
            return cost

    # 带备忘录的递归
    d = dict()

    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0

        # 最大代价为无限大，如果找到了比无限大小的，即说明可以换零钱
        cost = float('inf')
        # 对每个coin都进行计算，如果全是小于0的，则说明此路不通，并且最后返回cost
        for coin in coins:
            # 如果减去后小于0，说明以这种方式换零钱不对，金额不可达
            if amount - coin < 0:
                continue
            # 计算减去coin后，还需要的硬币数量
            if amount - coin in self.d:
                sub_amount = self.d[amount - coin]
            else:
                sub_amount = self.coinChange(coins, amount - coin)
                self.d[amount - coin] = sub_amount
            # 如果发现获得的下层节点得到的是-1，表示已经发生金钱不可达的情况，不再考虑
            if sub_amount == -1:
                continue
            # 求出最小代价
            cost = min(sub_amount + 1, cost)
        # 如果发现金钱不可达，返回-1
        if cost == float('inf'):
            return -1
        else:
            return cost

    # 动态规划
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost
        print(res)
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    # coins = [2]

    x = Solution()
    print(x.coinChange2(coins, 25))
