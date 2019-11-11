class Solution:
    def countAndSay(self, n: int) -> str:
        a = '1'
        for i in range(n - 1):
            a = self.count_next(a)
        return a


    def count_next(self, s):
        new_str = str()
        pre = s[0]
        num = 1
        for i in s[1:]:
            next = i
            if pre == next:
                num += 1
            else:
                new_str += str(num)
                new_str += pre
                num = 1
                pre = next
        new_str += str(num)
        new_str += pre
        return new_str


if __name__ == '__main__':
    x = Solution()

    a = 5
    print(x.countAndSay(a))

