class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)
        n = n[2:]
        # n = str(n)
        num = 0
        for i in n:
            if i == '1':
                num+=1
        return num

if __name__ == '__main__':
    x = Solution()

