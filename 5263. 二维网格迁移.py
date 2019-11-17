class Solution:
    def shiftGrid(self, grid, k: int):
        size = len(grid) * len(grid[0])
        k = k % size

        g = list()
        for i in grid:
            g.extend(i)
        g = g[-k:] + g[:size - k]


        g2 = list()
        for i in range(0, size, len(grid[0])):
            g2.append(g[i:i + len(grid[0])])
        return g2
