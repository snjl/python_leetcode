import time


class Solution:
    d = dict()

    # 递归方法
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    # 备忘录递归
    def fib2(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        if N in self.d.keys():
            return self.d[N]
        else:
            result = self.fib2(N - 1) + self.fib2(N - 2)
            self.d[N] = result
            return result

    # 动态规划方法
    def fib3(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        prev = 0
        curr = 1
        sum = 0
        for i in range(N - 1):
            sum = curr + prev
            prev = curr
            curr = sum
        return sum


if __name__ == '__main__':
    x = Solution()
    start = time.time()
    # print(x.fib(40))
    # # 40,用时43.14s
    # print(time.time() - start)

    print(x.fib2(40))
    print((time.time() - start))
    print(x.fib3(40))
