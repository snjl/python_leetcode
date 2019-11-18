class Solution:
    def sortArrayByParity(self, A):
        i = 0
        j = len(A) - 1

        while i != j:
            # 奇数，直接扔最后
            if A[i] % 2 != 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                j -= 1
            else:
                i += 1
        return A


if __name__ == '__main__':
    x = Solution()

    A = [3,1,2,4]
    print(x.sortArrayByParity(A))

