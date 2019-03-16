class Solution1:
    def isValid(self, s: str) -> bool:
        d = {
            '[': ']',
            '{': '}',
            '(': ')',
            ']': '',
            '}': '',
            ')': ''
        }
        len_s = len(s)
        half_len = int(len_s / 2)
        for i in range(half_len):
            if d[s[i]] == s[len_s - i - 1]:
                continue
            else:
                return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '[': ']',
            '{': '}',
            '(': ')',
        }
        len_s = len(s)
        l = list()
        for i in range(len_s):
            if s[i] not in [')','}',']']:
                l.append(s[i])
            else:
                if len(l) == 0:
                    return False
                if d[l.pop()] != s[i]:
                    return False
        if len(l) != 0:
            return False
        return True

if __name__ == '__main__':
    s = '[{)(}][{()}]'
    sl = Solution()
    print(sl.isValid(s))
