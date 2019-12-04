class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(i) for i in date.split('-')]

        m = dict()
        for i in [1, 3, 5, 7, 8, 10, 12]:
            m[i] = 31
        for i in [4, 6, 9, 11]:
            m[i] = 30
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            m[2] = 29
        else:
            m[2] = 28
        num = 0
        for i in range(1, month):
            num += m[i]
        num += day
        return num


if __name__ == '__main__':
    x = Solution()

    date = "2019-02-10"

    print(x.dayOfYear(date))

