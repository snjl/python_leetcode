import collections


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        max_area = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    area = self.bfs(i, j, height, width, grid)
                    if area > max_area:
                        max_area = area
        return max_area

    def bfs(self, i, j, height, width, grid):
        index1 = [0, 0, 1, -1]
        index2 = [1, -1, 0, 0]

        q = collections.deque()
        q.appendleft((i, j))
        area = 0
        while len(q):
            # print(q)
            x, y = q.pop()
            area += 1
            # 在第一次进入时进行标记，防止访问回来，多加一次
            grid[x][y] = 0
            for k in range(4):
                _x = x + index1[k]
                _y = y + index2[k]
                if 0 <= _x < height and 0 <= _y < width and grid[_x][_y] == 1:
                    # print(_x,_y)
                    # 在每次选择新加入的节点时也进行标记
                    grid[_x][_y] = 0
                    q.appendleft((_x, _y))
        # print('--------')
        return area


if __name__ == '__main__':
    x = Solution()
    l = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    l = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    l = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    # l = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    print(x.maxAreaOfIsland(l))
