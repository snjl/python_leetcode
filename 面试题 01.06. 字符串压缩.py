class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 0:
            return S
        s2 = ''

        now_c = None
        count = 0
        for i in S:
            if now_c is None:
                now_c = i
                count += 1
                continue
            elif now_c == i:
                count += 1
            else:
                s2 += now_c
                s2 += str(count)
                now_c = i
                count = 1
        s2 += now_c
        s2 += str(count)
        if len(s2) >= len(S):
            return S
        else:
            return s2

        pass

if __name__ == '__main__':
    x = Solution()

    print(x.compressString('aabcccccaaa'))