class Solution:

    length = 0
    wide = 0
    word = list()
    judge = False

    def exist(self, board, word: str) -> bool:
        self.length = len(board)
        self.wide = len(board[0])
        self.word = word

        return self.judge


        pass

    def dfs(self, board, path):
        if self.judge is True:
            return True

        for i in range(self.length):
            for j in range(self.wide):
                # if board[i][j]
                pass


if __name__ == '__main__':
    x = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"


    print(x.exist(board,word))
