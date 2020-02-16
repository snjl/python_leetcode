class Solution:
    def dailyTemperatures1(self, T):
        result = list()
        for i in range(len(T)):
            flag = False
            for j in range(i, len(T)):
                if T[j] > T[i]:
                    result.append(j - i)
                    flag = True
                    break
            if flag is False:
                result.append(0)

        return result

    # 递减栈（单调栈）
    def dailyTemperatures(self, T):
        result = [0 for _ in T]
        stack = list()
        for index, temp in enumerate(T):
            # 维护递减栈
            if len(stack) == 0 or stack[-1][1] >= temp:
                stack.append((index, temp))
            else:
                while len(stack) > 0 and stack[-1][1] < temp:
                    i, min_temp = stack.pop()
                    result[i] = index - i
                stack.append((index, temp))
        return result


if __name__ == '__main__':
    x = Solution()
    l = [73, 74, 75, 71, 69, 72, 76, 73]
    print(x.dailyTemperatures(l))
