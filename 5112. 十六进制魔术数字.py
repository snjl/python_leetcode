class Solution:
    def toHexspeak(self, num: str) -> str:
        t16 = hex(int(num))[2:]

        m = {'a': "A", 'b': "B", 'c': "C", 'd': "D", 'e': "E", 'f': "F", '1': "I", '0': "O"}
        new_t16 = ''
        for i in t16:
            if i not in m:
                return "ERROR"
            new_t16+=m[i]
        return new_t16



if __name__ == '__main__':
    x = Solution()
    num = "257"
    print(x.toHexspeak(num))