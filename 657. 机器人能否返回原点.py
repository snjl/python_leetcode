import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = collections.Counter(moves)
        if d.get('U',0) == d.get('D',0) and d.get('L',0) == d.get('R',0):
            return True
        else:
            return False

    def judgeCircle2(self, moves: str) -> bool:
        return moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D")

    def judgeCircle3(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0