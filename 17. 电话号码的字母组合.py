class Solution:
    # def letterCombinations(self, digits: str):
    #     if not digits: return []
    #     dic = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
    #     ans = []
    #     path = []
    #
    #     def backtrack(string):
    #         # 回溯终止条件：path长度和输入字符一样长
    #         if len(path) == len(digits):
    #             # 由于path的添加方式，此处需要重新组合成str
    #             ans.append(''.join(path[:]))
    #             return
    #
    #         # 每到一个节点，选择列表就是当前数字所表示的字母
    #         for char in dic[string[0]]:
    #             path.append(char)
    #             backtrack(string[1:])
    #             path.pop()
    #     backtrack(digits)
    #     return ans

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        dic = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz'}
        ans = []

        def dfs_digit(s, now_ans):
            if len(now_ans) == len(digits):
                ans.append(''.join(now_ans))
                return

            for i in dic[s[0]]:
                now_ans.append(i)
                dfs_digit(s[1:], now_ans)
                now_ans.pop()

        dfs_digit(digits, [])
        return ans


if __name__ == '__main__':
    x = Solution()
    digits = "234"

    print(x.letterCombinations(digits))
