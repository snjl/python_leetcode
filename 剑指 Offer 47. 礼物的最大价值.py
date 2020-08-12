class Solution:
    def maxValue(self, grid) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    x = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print(x.maxValue(grid))
