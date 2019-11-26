class Solution:
    def fraction(self, cont):
        cont = cont[::-1]
        # 第一次的分子分母
        fenzi = 1
        fenmu = cont[0]
        for i in range(1, len(cont)):
            fenzi = fenmu * cont[i] + fenzi
            fenmu, fenzi = fenzi, fenmu
            print(fenzi, fenmu)
        fenmu, fenzi = fenzi, fenmu

        return fenzi, fenmu


if __name__ == '__main__':
    x = Solution()

    # print(x.fraction([3, 2, 0, 2]))
    print(x.fraction([0,0,3]))
