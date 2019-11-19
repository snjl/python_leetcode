class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)
        y = bin(y)
        x = x[2:]
        y = y[2:]
        # 得到最长的长度
        l = max(len(x), len(y))
        # 补全长度
        x = self.add_zero(x, l)
        y = self.add_zero(y, l)

        num = 0
        for i in range(l):
            if x[i] != y[i]:
                num += 1
        return num
    # 补全前置空缺的0
    def add_zero(self, s, l):
        while len(s) < l:
            s = '0' + s
        return s
