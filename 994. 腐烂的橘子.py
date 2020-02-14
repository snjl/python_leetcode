import collections


class Solution:
    def orangesRotting(self, grid) -> int:
        good = 0
        # 记录是否遍历过该节点
        track_grid = list()
        time = -1
        q = collections.deque()
        for i in range(len(grid)):
            track_grid.append([0 for _ in range(len(grid[0]))])
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.appendleft((i, j))
                    track_grid[i][j] = 1
                elif grid[i][j] == 1:
                    good += 1
        if good == 0:
            return 0

        while len(q):
            time += 1
            size = len(q)
            for _ in range(size):
                x, y = q.pop()
                track_grid[x][y] = 1
                if x-1 >= 0 and grid[x - 1][y] == 1 and track_grid[x - 1][y] == 0:
                    track_grid[x - 1][y] = 1
                    q.appendleft((x - 1, y))
                    good -= 1
                if x + 1 <= len(grid) - 1 and grid[x + 1][y] == 1 and track_grid[x + 1][y] == 0:
                    track_grid[x + 1][y] = 1
                    q.appendleft((x + 1, y))
                    good -= 1
                if y - 1 >= 0 and grid[x][y - 1] == 1 and track_grid[x][y - 1] == 0:
                    track_grid[x][y - 1] = 1
                    q.appendleft((x, y - 1))
                    good -= 1
                if y + 1 <= len(grid[0]) - 1 and grid[x][y + 1] == 1 and track_grid[x][y + 1] == 0:
                    track_grid[x][y + 1] = 1
                    q.appendleft((x, y + 1))
                    good -= 1
        if good > 0:
            return -1
        else:
            return time
