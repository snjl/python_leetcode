class Solution(object):
    def reconstructMatrix2(self, upper, lower, colsum):
        m = len(colsum)
        colsum2 = [i for i in colsum]
        x = [colsum2, [0 for _ in range(m)]]

        for i in range(m):
            # 在0时返回0，在1时返回0,1，在2时返回0,1,2
            for j in range(colsum[i] + 1):
                x[0][i] = colsum[i] - j

                x[1][i] = j
                one = x[0]
                two = x[1]
                if sum(one) == upper and sum(two) == lower:
                    return x
        return list()

    def reconstructMatrix3(self, upper, lower, colsum):
        m = len(colsum)
        colsum2 = [i for i in colsum]
        x = [colsum2, [0 for _ in range(m)]]
        sum_lower_upper = upper + lower

        if sum([sum(x[0]), sum(x[1])]) != sum_lower_upper:
            print([])

        for i in range(m):
            if sum(x[0]) - upper <= 2:

                for j in range(colsum[i] + 1):
                    x[0][i] = colsum[i] - j
                    x[1][i] = j
                    if sum(x[0]) == upper and sum(x[1]) == lower:
                        return x
            else:
                x[0][i] = 0
                x[1][i] = colsum[i]
                if sum(x[0]) == upper and sum(x[1]) == lower:
                    return x
        return list()

    def reconstructMatrix(self, upper, lower, colsum):
        m = len(colsum)
        x = [[0 for _ in range(m)] for i in range(2)]

        sum_lower_upper = upper + lower

        if sum(colsum) != sum_lower_upper:
            return list()

        sum_upper = 0
        for i in range(m):
            if upper - sum_upper >= 2:
                x[0][i] = colsum[i]
                sum_upper += colsum[i]
            elif upper - sum_upper == 1:
                # 如果该列和大于等于1
                if colsum[i] >= 1:
                    x[0][i] = 1
                    x[1][i] = colsum[i] - 1
                    sum_upper += 1

                else:
                    pass
            # 此时第一行已经凑好
            else:
                x[1][i] = colsum[i]

        return x


if __name__ == '__main__':
    w = Solution()

    # upper = 5
    # lower = 5
    # colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]

    upper = 3
    lower = 3
    colsum = [0, 1, 1, 0, 1, 0, 2, 1]

    print(w.reconstructMatrix(upper, lower, colsum))
