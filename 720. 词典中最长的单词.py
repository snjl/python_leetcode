class Solution:
    def longestWord(self, words) -> str:
        max_len = max([len(word) for word in words])
        words2 = list()
        for i in range(max_len):
            len_words = [word for word in words if len(word) == max_len - i]
            if len_words:
                len_words.sort()
                words2.extend(len_words)

        for word in words2:
            split_word = word
            while len(split_word) != 0:
                if split_word in words:
                    split_word = split_word[:-1]
                else:
                    break
            if len(split_word) == 0:
                return word
            else:
                continue

        return ''


if __name__ == '__main__':
    x = Solution()
    words=  ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(x.longestWord(words))