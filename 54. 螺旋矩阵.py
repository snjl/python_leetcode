class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return list()

        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        new_matrix = list()

        while top <= bottom and left <= right:
            for i in range(left, right + 1, 1):
                new_matrix.append(matrix[top][i])
            for i in range(top + 1, bottom + 1, 1):
                new_matrix.append(matrix[i][right])

            # 如果刚好top==bottom或者是left==right，实际上经过上面的从左到右、从上到下已经将其遍历完了，不需要再次进行遍历
            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    new_matrix.append(matrix[bottom][i])
                for i in range(bottom - 1, top, -1):
                    new_matrix.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return new_matrix