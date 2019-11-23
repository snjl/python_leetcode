class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i in m.keys():
                m[i] += 1
        return min(m['b'], m['a'], int(m['l'] / 2), int(m['o'] / 2), m['n'])


if __name__ == '__main__':
    x = Solution()
    print(x.maxNumberOfBalloons( "loonbalxballpoon"))
