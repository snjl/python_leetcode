from queue import Queue


class Solution:
    # 广度优先
    def numIslands1(self, grid):
        count = 0
        if len(grid) == 0:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    q = Queue()
                    q.put([i, j])
                    count += 1
                    while q.empty() is False:
                        g = q.get_nowait()
                        new_x = g[0]
                        new_y = g[1]
                        if grid[new_x][new_y] == '1':
                            grid[new_x][new_y] = '0'
                            # q.put([g[0], g[1]])
                            if new_x - 1 >= 0 and grid[new_x - 1][new_y] == '1':
                                q.put_nowait([new_x - 1, new_y])
                            if new_y - 1 >= 0 and grid[new_x][new_y - 1] == '1':
                                q.put_nowait([new_x, new_y - 1])
                            if new_x + 1 < len(grid) and grid[new_x + 1][new_y] == '1':
                                q.put_nowait([new_x + 1, new_y])
                            if new_y + 1 < len(grid[0]) and grid[new_x][new_y + 1] == '1':
                                q.put_nowait([new_x, new_y + 1])
                        else:
                            continue
                        print(q.queue)
        return count

    # 深度优先
    def numIslands(self, grid):
        count = 0
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    stack = list()
                    stack.append((i, j))
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                            grid[x][y] = 0
                            stack.append((x + 1, y))
                            stack.append((x - 1, y))
                            stack.append((x, y + 1))
                            stack.append((x, y - 1))
                        else:
                            continue
        return count


if __name__ == '__main__':
    x = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    xx = list()
    for line in x:
        xx.append([str(i) for i in line])
    print(xx)
    s = Solution()

    print(s.numIslands(xx))
