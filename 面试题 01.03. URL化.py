class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        i = length - 1
        S = list(S)

        j = len(S) - 1
        while i >= 0:
            if S[i] == ' ':
                S[j] = '0'
                j -= 1
                S[j] = '2'
                j -= 1
                S[j] = '%'
                j -= 1
            else:
                S[j] = S[i]
                j -= 1
            i -= 1

        return ''.join(S)[j+ 1:]



if __name__ == '__main__':
    x = Solution()

    print(x.replaceSpaces("ds sdfs afs sdfa dfssf asdf             ",27))
