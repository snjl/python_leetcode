class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowers = 0
        # 统计1之间0的个数
        skip = 0
        flag = False
        # 对开头优化，加一个0，则和后面计算方法相同
        flowerbed = [0,] + flowerbed
        for index, flower in enumerate(flowerbed):
            if flower == 0:
                flag = True
                skip += 1
            else:
                if flag is True:
                    if skip > 2:
                        flowers += int((skip - 1) / 2)

                    skip = 0
                    flag = False
        # 对结尾优化，如果有0，则使用skip/2即可
        flowers += int(skip / 2)

        if flowers >= n:
            return True
        else:
            return False


if __name__ == '__main__':
    x = Solution()
    flowerbed = [0,0,1,0,1]
    n = 1
    print(x.canPlaceFlowers(flowerbed, n))
