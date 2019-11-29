import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        m = collections.Counter(s)
        # 按值排序
        m=sorted(m.items(), key=lambda v: v[1],reverse=True)
        new_s = ''
        for k, v in m:
            new_s += v * k
            print(k,v)
        return new_s

    # 桶排序
    def frequencySort2(self, s: str) -> str:
        m = collections.Counter(s)
        buckets_len = len(s)
        buckets = [[] for _ in range(buckets_len + 1)]
        for key, v in m.items():
            buckets[v].append(key)
        x = ''
        for i in range(buckets_len, -1, -1):
            if len(buckets[i]) > 0:
                for ss in buckets[i]:
                    x = x + ss * i

        return x


if __name__ == '__main__':
    s = "raaeaedere"
    x = Solution()

    print(x.frequencySort2(s))

