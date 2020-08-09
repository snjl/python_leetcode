class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        min_prices = [0 for _ in prices]
        min_prices[0] = prices[0]
        max_price = 0
        for i in range(1, len(prices)):
            min_prices[i] = min(prices[i], min_prices[i-1])
            max_price = max(max_price, prices[i] - min_prices[i])
        return max_price


if __name__ == '__main__':
    x = Solution()

    print(x.maxProfit([1]))


