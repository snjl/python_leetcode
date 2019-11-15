class Solution:
    def sortArrayByParityII(self, A):
        b = A.copy()

        odd = 1
        even = 0
        for i in A:
            if i % 2 == 0:
                b[even] = i
                even += 2
            else:
                b[odd] = i
                odd += 2
        return b

if __name__ == '__main__':
    x = Solution()

    A = [4,2,5,7]
    print(x.sortArrayByParityII(A))
