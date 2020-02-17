class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # write your code here
        offset = n % len(s)

        x1 = s[:offset]
        x2 = s[offset:]

        return x2+x1

if __name__ == '__main__':
    x = Solution()
    # s = "abcdefg"
    s = "lrloseumgh"
    k = 6
    print(x.reverseLeftWords(s,k))