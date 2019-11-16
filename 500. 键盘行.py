class Solution:
    def findWords(self, words):
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        d = dict()

        line_words = list()
        for i in s1:
            d[i] = 1
        for i in s2:
            d[i] = 2
        for i in s3:
            d[i] = 3

        for word in words:
            word2 = word.lower()
            if len(word2) <=1:
                line_words.append(word2)
            else:
                flag = 1
                n = d[word2[0]]
                for i in word2[1:]:
                    if d[i]!= n:
                        flag = 0
                        break
                if flag == 1:

                    line_words.append(word)
        return line_words