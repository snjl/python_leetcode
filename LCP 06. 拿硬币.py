class Solution:
    def minCount(self, coins) -> int:
        count = 0
        for i in coins:
            if i % 2 == 0:
                pass
            else:
                i += 1
            count += int(i / 2)

        return count

        pass


if __name__ == '__main__':
    x = Solution()
    print(x.minCount([2, 3, 10]))
