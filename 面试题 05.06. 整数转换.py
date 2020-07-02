class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        if A == B:
            return 0
        if A < 0:  # 对于负数，需要将A与全1的32位 与
            A &= 0xffffffff
        if B < 0:
            B &= 0xffffffff
        xor = A ^ B
        count = 0
        while xor != 0:
            xor = xor & (xor - 1)
            count += 1
        return count  # 数 1 的个数

        # return str(bin(A ^ B)).count("1")  # 另一种方法数1的个数






if __name__ == '__main__':
    x = Solution()

    print(x.convertInteger(-5, -6))
