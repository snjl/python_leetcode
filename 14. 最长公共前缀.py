class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ''
        if len(strs) == 0:
            return prefix
        l = min([len(i) for i in strs])
        for i in range(l):
            same_char = strs[0][i]
            same_flag = True
            for s in strs[1:]:
                if same_char != s[i]:
                    same_flag = False
                    break
            # 如果表示不同
            if same_flag is False:
                return prefix
            else:
                prefix += same_char
        return prefix







if __name__ == '__main__':
    x = Solution()
    strs = ["flower","flow","flight"]
    strs = [""]
    print(x.longestCommonPrefix(strs))


