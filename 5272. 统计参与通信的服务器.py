class Solution:
    def countServers(self,grid) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = 0
                    # 检测行
                    for k in range(len(grid)):
                        if k != i and grid[k][j] == 1:
                            count += 1
                            flag = 1
                            break
                    # 如果行未检测到，检测列
                    if flag == 0:
                        for k in range(len(grid[0])):
                            if k != j and grid[i][k] == 1:
                                count += 1
                                break
        return count
if __name__ == '__main__':
    x= Solution()

    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    # grid = [[1, 0], [1, 1]]
    # grid = [[1, 0], [0, 1]]

    print(x.countServers(grid))