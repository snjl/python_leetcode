class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        l = text.split(' ')
        if len(l)<=2:
            return list()
        r = list()
        # 只匹配到倒数第二个字符串，由于要一次匹配2个，所以匹配到倒数第三个字符串即可
        for i in range(len(l) - 2):
            if l[i] == first and l[i+1] == second:
                r.append(l[i+2])
        return r


        pass



if __name__ == '__main__':
    x = Solution()

    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    print(x.findOcurrences(text,first,second))
