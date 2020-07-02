class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        l = list()
        for i in range(left, right + 1):
            dividing = True
            i_str = str(i)
            for s in i_str:
                if s == '0':
                    dividing = False
                    break
                if i % int(s) != 0:
                    dividing = False
                    break
            if dividing is True:
                l.append(i)
        return l



if __name__ == '__main__':
    x = Solution()
    print(x.selfDividingNumbers(1,22))