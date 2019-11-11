import collections


class Solution:
    def isAnagram(self, s, t):
        s_d = collections.Counter(s)
        t_d = collections.Counter(t)
        if s_d == t_d:
            return True
        else:
            return False
