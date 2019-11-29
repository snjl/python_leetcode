import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_m = collections.Counter(s)
        t_m = collections.Counter(t)
        for k,v in s_m.items():
            if t_m[k] == s_m[k]:
                t_m.pop(k)
            else:
                return k
        for k,_ in t_m.items():
            return k
    '''
    python 3.2之后
    collections.Counter 提供了加减方法。
    Counter(t) - Counter(s)后返回值就是多出来的字母，list()后返回即可。
    '''


    def findTheDifference2(self, s: str, t: str) -> str:
        return list(collections.Counter(t) - collections.Counter(s))[0]

