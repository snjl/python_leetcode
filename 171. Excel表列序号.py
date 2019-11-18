class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for i in s:
            num = num * 26 + (ord(i) - 64)
        return num