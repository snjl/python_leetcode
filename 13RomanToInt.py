
class Solution1:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        s_len = len(s)
        for i, symbol in enumerate(s):
            if i < s_len - 1:
                if roman_dict[symbol] >= roman_dict[s[i + 1]]:
                    sum += roman_dict[symbol]
                else:
                    sum -= roman_dict[symbol]
            else:
                sum += roman_dict[symbol]
        return sum

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        s_len = len(s)
        for i in range(s_len - 1):
            sum += roman_dict[s[i]]
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                sum -= roman_dict[s[i]] * 2
        sum += roman_dict[s[-1]]
        return sum

if __name__ == '__main__':
    s1 = Solution()
    print(s1.romanToInt('MCMXCIV'))


