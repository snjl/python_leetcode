class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0:
            return []
        M, N, result = len(matrix), len(matrix[0]), []
        for curve_line in range(M + N - 1):
            row_begin = 0 if curve_line + 1 <= N else curve_line + 1 - N
            row_end = M - 1 if curve_line + 1 >= M else curve_line
            if curve_line % 2 == 1:
                for i in range(row_begin, row_end + 1):
                    result.append(matrix[i][curve_line - i])
            else:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][curve_line - i])
        return result


if __name__ == '__main__':
    x = Solution()

    matrix = [
        [1, 2, 3,10],
        # [4, 5, 6,10],
        # [7, 8, 9,10]
    ]

    print(x.findDiagonalOrder(matrix))