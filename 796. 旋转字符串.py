class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and A == "":
            return True
        for i in range(len(A)):
            A = self.reverseLeftWords(A, 1)
            if A == B:
                return True
        return False

    def reverseLeftWords(self, s: str, n: int) -> str:
        # write your code here
        offset = n % len(s)

        x1 = s[:offset]
        x2 = s[offset:]

        return x2 + x1
