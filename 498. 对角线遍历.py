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

    # 超时方法
    def findDiagonalOrder2(self, matrix):
        if len(matrix) == 0:
            return []
        # 表示按行从右到左，按列从上到下，flag=1表示按行从左到右，按列从下到上
        flag = 0
        M, N, result = len(matrix), len(matrix[0]), []

        for i in range(M + N - 1):
            if flag == 0:
                # j表示按列从上到下算
                for j in range(i + 1):
                    # 保证j和i-j都在N和M的范围内
                    if j < N and i - j < M:
                        result.append(matrix[i - j][j])
                        # print([i - j, j], end=' ')
                flag = 1
            else:
                # k表示按行从左到右算
                for k in range(i + 1):
                    # 保证k和i-k都在M和N的范围内
                    if k < M and i - k < N:
                        result.append(matrix[k][i - k])
                        # print([k, i - k], end=' ')
                flag = 0
            # print()
        return result


if __name__ == '__main__':
    x = Solution()

    matrix = [
        [1, 2, 3, 10],
        [4, 5, 6, 10],
        [7, 8, 9, 10]
    ]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

