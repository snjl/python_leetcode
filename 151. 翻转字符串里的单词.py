class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        s_split = [i for i in s_split if i != '']
        s_split = s_split[::-1]
        return ' '.join(s_split)

    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    x = Solution()

    s = "a good   example"
    print(x.reverseWords2(s))
