class Solution:
    def climbStairs2(self, n: int) -> int:
        i = 1    # 爬到1台阶仅有1种方法
        j = 2    # 爬到2台阶有2种方法
        for _ in range(3, n):         # 自底向上递推 F(n)=F(n-1)+F(n-2)
            i, j = j, i + j           # 每次仅保留前两个值，依次往后推算
        return i + j if n > 2 else n  # 注意当n=1,n=2时的情况


    def climbStairs(self, n: int) -> int:
        if n== 0:
            return 1
        if n == 1:
            return 1

        l = [0 for _ in range(n + 1)]
        l[0] = 1
        l[1] = 1
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[-1]



if __name__ == '__main__':

    x = Solution()

    print(x.climbStairs(10))