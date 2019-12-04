class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        l = list()

        for word in words:
            if self.findPattern(word,pattern):
                l.append(word)
        return l

    def findPattern(self,word,pattern):
        if len(word) != len(pattern):
            return False
        m = dict()
        for i in range(len(pattern)):
            if pattern[i] not in m.keys():
                # 保证是双射
                if word[i] in m.values():
                    return False
                else:
                    m[pattern[i]] = word[i]

            else:
                if m[pattern[i]] != word[i]:
                    return False

        return True


if __name__ == '__main__':
    x = Solution()
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(x.findAndReplacePattern(words,pattern))



