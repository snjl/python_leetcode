class Solution:
    def sortByBits(self, arr):
        m = dict()
        for i in arr:
            i_bin = bin(i)[2:]
            count = 0
            for j in i_bin:
                if j == '1':
                    count += 1
            if count in m.keys():
                m[count].append(i)
            else:
                m[count] = list()
                m[count].append(i)
        l = list()

        keys = list(m.keys())
        keys.sort()
        for i in keys:
            m[i].sort()
            l.extend(m[i])

        return l



if __name__ == '__main__':
    x = Solution()

    arr = [10,100,1000,10000]

    print(x.sortByBits(arr))
