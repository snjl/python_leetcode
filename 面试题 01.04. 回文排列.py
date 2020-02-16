class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = dict()
        for i in s:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        x = 0
        for v in m.values():
            if v % 2 == 1:
                x += 1
                if x > 1:
                    return False

        return True
