class Solution(object):
    def oddCells(self, n, m, indices):
        x = [[0 for _ in range(m)] for _ in range(n)]
        # [a,b]表示第a行+1，第b列+1
        for indice in indices:
            for i in range(m):
                x[indice[0]][i] += 1
            for i in range(n):
                x[i][indice[1]] += 1
        # print(x)

        num = 0
        for i in range(n):
            for j in range(m):
                if x[i][j] % 2 == 1:
                    num += 1
        return num

if __name__ == '__main__':
    w = Solution()
    # n = 2
    # m = 3
    # indices = [[0, 1], [1, 1]]
    n = 2
    m = 2
    indices = [[1, 1], [0, 0]]


    print(w.oddCells(n,m,indices))

