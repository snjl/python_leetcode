class Solution:
    def numberOfLines(self, widths, S: str):
        num = 0
        hang = 1
        for i in S:
            num += (widths[ord(i) - 97])
            if num> 100:
                num = 0
                num += (widths[ord(i) - 97])
                hang +=1
        return [hang,num]


if __name__ == '__main__':
    x = Solution()

    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print(x.numberOfLines(widths, S))
