class Solution:
    def restoreString(self, s: str, indices) -> str:
        l = [0 for _ in s]
        for i in indices:
            l[indices[i]] = s[i]
        return ''.join(l)

        pass