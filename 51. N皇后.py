class Solution:
    def solveNQueens(self, n: int):
        l = list()

        def is_valid(m, row, col):
            # print(row, col)
            # 横
            for i in range(len(m)):
                if m[i][row] == 'Q':
                    return False
            # 竖
            for i in range(len(m)):
                if m[col][i] == 'Q':
                    return False
            col_pos = col
            # 左上
            # for i in range(row, -1, -1):
            #     if m[i][col_pos] == 'Q':
            #         return False
            #     col_pos = col_pos - 1
            #
            # col_pos = col
            # # 右上
            # for i in range(row, -1, -1):
            #     if col_pos >= len(m) - 1:
            #         break
            #     if m[i][col_pos] == 'Q':
            #         return False
            #     col_pos = col_pos + 1
            return True

        def dfs(row, m):
            # print(m)
            # b = m.copy()
            if row == n:
                print(row)
                print(m)
                l.append(m[:])
                return
            for col in range(n):
                # 如果这个位置可以放，则继续，不可以放则剪枝
                if is_valid(m, row, col):
                    m[row][col] = 'Q'
                    dfs(row + 1, m.copy())
                    m[row][col] = '.'
                # print(row, col)

        first_m = [['.' for _ in range(n)] for _ in range(n)]

        dfs(0, first_m)
        return l
        pass


# 疑似有内存泄漏
if __name__ == '__main__':
    x = Solution()
    print(x.solveNQueens(4))
