class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = list()
        last = s[0]
        count = 1
        for i in s[1:]:
            if i == last:
                count += 1
            else:
                l.append(count)
                count = 1
                last = i
        l.append(count)
        if len(l) == 1:
            return 0
        all_count = 0
        # print(l)
        for i in range(1, len(l)):
            all_count += min(l[i - 1], l[i])
        return all_count


if __name__ == '__main__':
    x = Solution()
    print(x.countBinarySubstrings("00110011"))
