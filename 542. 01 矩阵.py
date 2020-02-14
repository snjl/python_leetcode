import collections
import copy


class Solution:
    def updateMatrix(self, matrix):
        if len(matrix) == 0:
            return list()

        dis_matrix = copy.deepcopy(matrix)
        matrix_height = len(matrix)
        matrix_wide = len(matrix[0])
        for i in range(matrix_height):
            for j in range(matrix_wide):
                if matrix[i][j] == 0:
                    dis_matrix[i][j] = 0
                    continue
                q = collections.deque()
                q.appendleft((i, j))
                distance = -1
                while len(q):
                    size = len(q)
                    distance += 1
                    flag = False
                    for _ in range(size):
                        x, y = q.pop()
                        if 0 <= x < matrix_height and 0 <= y < matrix_wide:
                            if matrix[x][y] == 0:
                                dis_matrix[i][j] = distance
                                flag = True
                                break
                            else:
                                q.appendleft((x + 1, y))
                                q.appendleft((x - 1, y))
                                q.appendleft((x, y + 1))
                                q.appendleft((x, y - 1))

                    if flag is True:
                        break
        return dis_matrix


if __name__ == '__main__':
    x = Solution()
    l = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(x.updateMatrix(l))
