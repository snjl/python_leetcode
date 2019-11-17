class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        new_s = ' '.join([w[::-1] for w in s_split])
        return new_s