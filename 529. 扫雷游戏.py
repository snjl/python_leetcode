import collections


class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        height = len(board)
        if height == 0:
            return 0
        width = len(board[0])

        index1 = [-1, 0, 1, -1, 1, -1, 0, 1]
        index2 = [1, 1, 1, 0, 0, -1, -1, -1]
        q = collections.deque()
        q.append(click)
        while len(q) > 0:
            x, y = q.pop()
            if board[x][y] == 'E':
                count = 0
                for i in range(8):
                    _x = x + index1[i]
                    _y = y + index2[i]
                    if 0 <= _x < height and 0 <= _y < width:
                        # 附近有地雷M，count+1
                        if board[_x][_y] == 'M':
                            count += 1

                if count == 0:
                    board[x][y] = 'B'
                    for i in range(8):
                        _x = x + index1[i]
                        _y = y + index2[i]
                        if 0 <= _x < height and 0 <= _y < width:

                            q.appendleft((_x, _y))
                else:
                    board[x][y] = str(count)
        return board

if __name__ == '__main__':
    x = Solution()
    l = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]

    Click = [3, 0]
    print(x.updateBoard(l, Click))
