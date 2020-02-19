class Solution:
    matrix = None
    height = 0
    width = 0

    def searchMatrix(self, matrix, target: int) -> bool:
        self.matrix = matrix
        self.height = len(matrix)
        if self.height == 0:
            return False

        self.width = len(matrix[0])

        height = len(matrix)
        width = len(matrix[0])
        size = width * height
        left = 0
        right = size - 1

        for i in range(size):
            x, y = self.get_position(i)
            print(i,matrix[x][y], self.get_position(i))

        while left <= right:
            mid = int((left + right) / 2)
            x, y = self.get_position(mid)
            if matrix[x][y] < target:
                left = mid + 1
            elif matrix[x][y] > target:
                right = mid - 1
            else:
                return True
        return False

    def get_position(self, num):
        i = int(num / self.width)
        j = num - i * self.width

        return i, j


if __name__ == '__main__':
    x = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    target = 34
    print(x.searchMatrix(matrix, target))
