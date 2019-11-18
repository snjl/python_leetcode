class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x = 1

        top = 0
        left = 0
        right = n - 1
        bottom = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1, 1):
                matrix[top][i] = x
                x += 1
            for i in range(top + 1, bottom + 1, 1):
                matrix[i][right] = x
                x += 1

            # 如果刚好top==bottom或者是left==right，实际上经过上面的从左到右、从上到下已经将其遍历完了，不需要再次进行遍历
            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    matrix[bottom][i] = x
                    x += 1
                for i in range(bottom - 1, top, -1):
                    matrix[i][left] = x
                    x += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix