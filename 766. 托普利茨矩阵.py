class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        if len(matrix) == 1:
            return True

        for i in range(1, len(matrix)):
            if matrix[i - 1][:-1] == matrix[i][1:]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    x = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]



