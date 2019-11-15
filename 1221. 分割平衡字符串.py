class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        l_num = 0
        r_num = 0
        for i in s:
            if i == 'L':
                l_num += 1
            elif i == 'R':
                r_num += 1
            if l_num == r_num:
                num += 1
                l_num = 0
                r_num = 0
        return num

if __name__ == '__main__':
    x = Solution()

    s = "RLRRLLRLRL"
    s = "LLLLRRRR"

    print(x.balancedStringSplit(s))