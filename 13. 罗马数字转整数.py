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

        a = list()
        num = 0
        for i in range(len(s)):
            if len(a) == 0:
                num += roman_dict[s[i]]
                a.append(roman_dict[s[i]])

            else:
                last_num = a.pop(0)
                if last_num >= roman_dict[s[i]]:
                    num += roman_dict[s[i]]
                else:
                    num += roman_dict[s[i]]
                    num = num - last_num * 2
                a.append(roman_dict[s[i]])

        return num



if __name__ == '__main__':
    x = Solution()

    s = "LVIII"

    print(x.romanToInt(s))