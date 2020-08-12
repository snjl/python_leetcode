class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])

        p_x = n - 1
        p_y = 0

        while p_x >= 0 and p_y <= m - 1:
            if matrix[p_x][p_y] == target:
                return True
            elif matrix[p_x][p_y] > target:
                p_x -= 1
            else:
                p_y += 1
        return False


if __name__ == '__main__':
    x = Solution()
    # m = [
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    # t = 28

    m=[[-1,3]]
    t = 3
    print(x.findNumberIn2DArray(m, t))