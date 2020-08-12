class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        bin_n = bin(n)[2:]
        print(bin(n))
        one = 0
        for i in bin_n:
            if i == '1':
                one += 1
        if one == 1:
            return True
        return False



if __name__ == '__main__':
    x = Solution()
    print(x.isPowerOfTwo(128))
