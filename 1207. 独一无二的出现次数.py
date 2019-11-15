import collections

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        map = collections.Counter(arr)
        s = set()
        for v in map.values():
            if v in s:
                return False
            s.add(v)
        return True
if __name__ == '__main__':
    x = Solution()

    arr = [1, 2, 2, 1, 1, 3]
    arr = [1, 2, 2, 1, 1, 3, 2]

    print(x.uniqueOccurrences(arr))


