class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N-1,-1,-1):
            for c in range(N-1,-1,-1):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans


if __name__ == '__main__':
    x = Solution()
    print(x.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
