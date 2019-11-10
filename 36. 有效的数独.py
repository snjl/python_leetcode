class Solution:
    def isValidSudoku(self, board):
        for line in board:
            if self.never_same(line) is False:
                return False
        columns = self.get_columns(board)
        for line in columns:
            if self.never_same(line) is False:
                return False
        nine = self.get_nine(board)
        for line in nine:
            if self.never_same(line) is False:
                return False

        return True



    # 传入为某行，某列，某个九宫格的数据list，如果有相同的字符，则返回False
    def never_same(self,l):
        l = [int(i) for i in l if i != '.']
        return len(l) == len(set(l))


    # 获取列向量
    def get_columns(self,board):
        T_board = [list() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                T_board[i].append(board[j][i])
        return T_board


    def get_nine(self,board):
        range_list = [[0, 3], [3, 6], [6, 9]]
        a = [(i, j) for i in range_list for j in range_list]
        nine_list = list()
        for w in a:
            n = list()
            for i in range(w[0][0], w[0][1]):
                for j in range(w[1][0], w[1][1]):
                    n.append(board[i][j])

            nine_list.append(n)
        return nine_list


class Solution2:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    # print(s.isValidSudoku(board))