class Solution:
    def replaceSpace(self, s: str) -> str:
        n = ''
        for i in s:
            if i == ' ':
                n += '%20'
            else:
                n += i
        return n


