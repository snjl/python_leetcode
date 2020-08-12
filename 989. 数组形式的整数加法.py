class Solution:
    def addToArrayForm(self, A, K: int):
        A = A[::-1]
        while K > 0:
            n = K % 10
            K = int(K / 10)
            print(n, K)

        pass


if __name__ == '__main__':
    x = Solution()
    A = [1, 2, 0, 0]
    K = 4231

    print(x.addToArrayForm(A, K))
