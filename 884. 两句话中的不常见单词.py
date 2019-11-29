import collections

# 统计只出现一次的单词即可
class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        A =A + ' '+ B

        a = collections.Counter(A.split(' '))

        for k in list(a.keys()):
            if a[k] >1:
                a.pop(k)
        a = list(a.keys())

        return a

if __name__ == '__main__':
    x = Solution()

    A="apple apple"
    B="banana"
    print(x.uncommonFromSentences(A,B))



