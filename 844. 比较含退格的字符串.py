class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ''
        t = ''
        for i in S:
            if i == '#':
                if len(s) >0:
                    s = s[:-1]
            else:
                s +=i
        for i in T:
            if i == '#':
                if len(t) > 0:
                    t = t[:-1]
            else:
                t += i
        if s== t:
            return True
        else:
            return False
