class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        matrix[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i >= 1:
                    matrix[i][j] += matrix[i - 1][j]
                if j >= 1:
                    matrix[i][j] += matrix[i][j - 1]

        return matrix[n - 1][m - 1]


if __name__ == '__main__':
    x = Solution()

    # m = 7
    # n = 3
    m = 3
    n = 2
    print(x.uniquePaths(m, n))
