class Solution:
    def solve(self, board) -> None:
        # 将边缘的O以及与O相邻的部分都先转化为A，然后将其他O的部分转化为X，再把A的部分转化为O
        stack = list()
        if len(board) == 0:
            return

        board_height = len(board)
        board_wide = len(board[0])

        for i in range(board_height):
            for j in range(board_wide):
                if (i == 0 or j ==0 or i == board_height -1 or j == board_wide - 1) and board[i][j] == 'O':
                    stack.append((i,j))



        print(stack)
        while stack:
            x, y = stack.pop()
            if 0 <= x < board_height and 0 <= y < board_wide and board[x][y] == 'O':
                board[x][y] = 'A'
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

        for i in range(board_height):
            for j in range(board_wide):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        print(board)

if __name__ == '__main__':
    x = Solution()

    a = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    x.solve(a)
