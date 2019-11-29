import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        m = collections.Counter(nums)
        m = sorted(m.items(), key=lambda v: v[1], reverse=True)

        l = [k[0] for k in m]
        return l[:k]

    # 调用函数
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    # 桶排序，参考https://leetcode-cn.com/problems/top-k-frequent-elements/solution/tong-pai-xu-by-wmy1696/
    def topKFrequent3(self, nums, k: int):
        m = collections.Counter(nums)
        buckets_len = len(nums)
        buckets = [[] for _ in range(buckets_len + 1)]
        for key, v in m.items():
            buckets[v].append(key)
        x = list()
        for i in range(buckets_len, -1, -1):
            if len(buckets[i]) > 0:
                x.extend(buckets[i])
                if len(x) >= k:
                    return x[:k]
        return x


if __name__ == '__main__':
    x = Solution()
    # nums = [1, 2, 2, 2, 5, 5, 5, 5]
    nums = [-1,-1]
    k = 1

    print(x.topKFrequent3(nums, k))
