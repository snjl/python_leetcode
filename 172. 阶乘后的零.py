class Solution:
    def trailingZeroes2(self, n: int) -> int:
        # 出现1个2和1个5，则多1个0，但是2比5出现多，所以只要统计5即可
        # 实际上即按5的倍数找，找到一个则多一个0
        num = 0
        # 满足该流程则默认+1
        for i in range(0, n + 1, 5):
            # 统计i中5的个数
            while i%5 ==0 and i > 0:
                num += 1
                i /= 5
        return num

    def trailingZeroes(self, n: int) -> int:

        num = 0
        while n:
            num += (n // 5)
            n //= 5

        return num
if __name__ == '__main__':
    x = Solution()
    print(x.trailingZeroes(100))
