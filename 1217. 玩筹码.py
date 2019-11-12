class Solution(object):
    def minCostToMoveChips(self, chips):
        # 存储Q奇数、偶数的数量，奇数到奇数、偶数到偶数均不需要步骤
        a = [0, 0]
        for i in chips:
            if i % 2 == 0:
                a[1] += 1
            else:
                a[0] += 1
        return min(a)


if __name__ == '__main__':
    x = Solution()
    chips = [2, 2, 2, 3, 3]
    print(x.minCostToMoveChips(chips))
