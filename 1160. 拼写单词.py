import collections


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        chars_map = collections.Counter(chars)

        num = 0
        for word in words:
            count = True

            word_map = collections.Counter(word)
            for k,v in word_map.items():
                if v <= chars_map.get(k,0):
                    continue
                else:
                    count =False

            if count is True:
                num += len(word)
        return num


