class Solution:
    def transpose(self, A):
        B = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                B[j][i] = A[i][j]
        return B


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A =[[1, 2], [4, 5], [7, 8]]
    x =Solution()
    print(x.transpose(A))