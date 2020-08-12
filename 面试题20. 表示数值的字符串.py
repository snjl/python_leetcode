class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if s[0] == '+' or s[0] == '-':
            return False
        if 'e' in s or 'E' in s:
            if 'e' in s:
                first,second = s.split('e')
            if 'E' in s:
                first,second = s.split('E')

            pass

        pass



if __name__ == '__main__':
    x = Solution()
    print(x.isNumber('+100'))
