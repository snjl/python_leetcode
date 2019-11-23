class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        ms = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        s = set()

        for word in words:
            word = ''.join([ms[ord(i) - 97] for i in word])
            s.add(word)
        return len(s)


if __name__ == '__main__':
    x= Solution()

    words = ["gin", "zen", "gig", "msg"]

    print(x.uniqueMorseRepresentations(words))
