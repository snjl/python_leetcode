class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        w = ''
        flag = 0
        for i in S:
            if flag == 0 and i == '(':
                flag += 1
            elif flag > 0 and i == '(':
                w += i
                flag += 1
            elif flag > 1 and i == ')':
                w += i
                flag -= 1
            elif flag == 1 and i == ')':
                flag -= 1
        return w


if __name__ == '__main__':
    x = Solution()

    s = "(()())(())"
    s = "(()())(())(()(()))"
    s = "()()"

    print(x.removeOuterParentheses(s))