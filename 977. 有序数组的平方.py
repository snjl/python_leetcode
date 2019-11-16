class Solution:
    def sortedSquares(self, A):
        A = [abs(i) for i in A]
        A.sort()
        return [i **2 for i in A]
