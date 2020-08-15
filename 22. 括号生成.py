class Solution:
    def generateParenthesis(self, n: int):
        l = list()

        def dfs(m, left_num, right_num):
            if left_num == 0 and right_num == 0:
                l.append(m[:])
                # print(l)
                return

            # 左括号剩余数量大于右括号剩余数量，不合法
            if left_num > right_num:
                return
            if left_num < 0 or right_num < 0:
                return
            # 加一个左括号
            m += '('
            dfs(m, left_num - 1, right_num)
            m = m[:-1]
            # 加一个右括号
            m += ')'
            dfs(m, left_num, right_num - 1)

        dfs("", n, n)

        return l


if __name__ == '__main__':
    x = Solution()

    print(x.generateParenthesis(3))
