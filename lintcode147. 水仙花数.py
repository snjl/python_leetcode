class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def getNarcissisticNumbers(self, n):
        l = []  # 存放满足要求的水仙花数
        if n == 1:
            l.append(0)  # 如果n等于1，下面循环从range（1,10），少了0，所以先补上
        store = []
        for item in range(10):
            store.append(pow(item, n))  # 存放0-9的N次幂。这里先把N次幂算出来，下面要用的话就直接取，不会再每一个都算一遍

        for j in range(pow(10, n - 1), pow(10, n)):  # j表示几位数，例如n == 4，就是所有的四位数
            j_str = str(j)  # 先将整数j转换为字符串，方便依次取下标
            sums = 0
            for k in range(len(j_str)):
                sums += store[int(j_str[k])]  # 这里int（j_str）这里循环依次取出整数j的每一个数字
            if j == sums:
                l.append(j)
        return l


if __name__ == '__main__':
    x = Solution()
    print(x.getNarcissisticNumbers(4))
