class Solution:
    def maxProfit(self, prices) -> int:
        max_price = 0
        for i in range(1, len(prices)):
            now_price = prices[i]
            prices[i] = min(prices[i - 1], prices[i])
            max_price = max(max_price, now_price - prices[i])

        return max_price


if __name__ == '__main__':
    x = Solution()
    print(x.maxProfit([7, 6, 4, 3, 1]))
