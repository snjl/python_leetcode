class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import time

        start = time.mktime(time.strptime(date1, '%Y-%m-%d'))
        end = time.mktime(time.strptime(date2, '%Y-%m-%d'))

        count_days = int((end - start) / (24 * 60 * 60))

        return abs(count_days)


if __name__ == '__main__':
    x  = Solution()
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    print(x.daysBetweenDates(date1,date2))