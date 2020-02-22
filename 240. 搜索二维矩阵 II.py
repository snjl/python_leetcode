class Solution:

    def searchMatrix(self, matrix, target: int) -> bool:

        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])

        p_x = height - 1
        p_y = 0
        while p_x >= 0 and p_y < width:
            if matrix[p_x][p_y] == target:
                return True
            elif matrix[p_x][p_y] < target:
                p_y += 1
            else:
                p_x -= 1

        return False

if __name__ == '__main__':
    x = Solution()
    m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    t = 29
    print(x.searchMatrix(m,t))

