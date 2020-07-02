class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        m = list()
        for i in range(len(matrix)):

            m.extend(matrix[i])
        m.sort()
        return m[k - 1]

        pass


if __name__ == '__main__':
    x = Solution()

    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8

    print(x.kthSmallest(matrix, k))


