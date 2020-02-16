import collections


class Solution:
    def islandPerimeter(self, grid) -> int:
        index1 = [0, 1, 0, -1]
        index2 = [1, 0, -1, 0]
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        q = collections.deque()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    q.appendleft((i, j))
        perimeter = 0
        while len(q):
            x, y = q.pop()
            for i in range(4):
                if 0 <= x + index1[i] < height and 0 <= y + index2[i] < width:
                    if grid[x + index1[i]][y + index2[i]] == 0:
                        perimeter += 1
                else:
                    perimeter += 1
        return perimeter