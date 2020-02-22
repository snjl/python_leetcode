class Solution:
    def checkIfExist2(self, arr) -> bool:
        s = set()
        for i in arr:
            if i * 2 not in s:
                s.add(i)
            else:
                return True
        s = set()
        for i in arr[::-1]:
            if i * 2 not in s:
                s.add(i)
            else:
                return True
        return False

    def checkIfExist(self, arr) -> bool:
        s = set()
        zero_num = 0
        for i in arr:
            if i == 0:
                zero_num += 1
            else:
                s.add(i)
        if zero_num >= 2:
            return True
        for i in s:
            if i * 2 in s:
                return True
        return False


if __name__ == '__main__':
    x = Solution()
    a = [-2,0,10,-19,4,6,-8]
    print(x.checkIfExist(a))
