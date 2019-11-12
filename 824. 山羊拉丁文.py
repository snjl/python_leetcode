class Solution:
    yy = 'aeiouAEIOU'
    def toGoatLatin(self, S: str) -> str:
        words_list = list()
        for index, word in enumerate(S.split(' ')):
            new_word = self.wordToGoatLatin(word,index+1)
            words_list.append(new_word)

        return ' '.join(words_list)


    def wordToGoatLatin(self,word,pos):
        if word[0] in self.yy:
            return word + 'ma' + 'a' * pos
        else:
            return word[1:] + word[0] + 'ma' + 'a' * pos





if __name__ == '__main__':
    x = Solution()

    s = "over over over"
    print(x.toGoatLatin(s))





