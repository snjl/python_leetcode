class Solution:
    def groupAnagrams(self, strs):

        m = dict()
        for s in strs:
            sort_s = ''.join(sorted(s))
            if sort_s in m.keys():
                m[sort_s].append(s)
            else:
                m[sort_s] = [s, ]
        l = list()
        for v in m.values():
            l.append(v)
        return l


if __name__ == '__main__':
    x = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(x.groupAnagrams(strs))



