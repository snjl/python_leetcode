import collections


class Solution:
    def distributeCandies(self, candies) -> int:
        m = collections.Counter(candies)
        num = len(m)
        # 如果所有种类大于糖果一半，由于只能拿一半，所以返回一半
        if num > len(candies) // 2:
            return len(candies) // 2
        else:
            # 如果所有种类不大于糖果一半，则返回所有糖果种类数量
            return num


if __name__ == '__main__':
    x = Solution()
    candies = [1, 1, 2, 2, 3, 3]

    print(x.distributeCandies(candies))
