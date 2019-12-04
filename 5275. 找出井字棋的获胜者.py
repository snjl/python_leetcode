class Solution:
    def tictactoe(self, moves) -> str:

        A = [moves[i] for i in range(len(moves)) if i % 2 == 0]
        B = [moves[i] for i in range(len(moves)) if i % 2 == 1]

        x1 = self.win(A, 'A')
        x2 = self.win(B, 'B')

        if x1:
            return x1
        if x2:
            return x2

        if len(moves) == 9:
            return 'Draw'
        return 'Pending'


    def win(self,A,x):
        count = 0
        for i in range(3):
            if [i, i] in A:
                count += 1
        if count == 3:
            return x
        count = 0
        for i in range(3):
            if [i, 2-i] in A:
                count += 1
        if count == 3:
            return x
        for i in range(3):
            count = 0
            for j in range(3):
                if [i, j] in A:
                    count+=1
                if count == 3:
                    return x
        for i in range(3):
            count = 0
            for j in range(3):
                if [j, i] in A:
                    count+=1
                if count == 3:
                    return x
        return None

if __name__ == '__main__':
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    moves = [[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]
    A = [moves[i] for i in range(len(moves)) if i % 2 == 0]
    B = [moves[i] for i in range(len(moves)) if i % 2 == 1]

    x = Solution()
    print(x.tictactoe(moves))