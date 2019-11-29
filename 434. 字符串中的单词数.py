class Solution:
    def countSegments(self, s: str) -> int:
        x= s.strip()
        if len(x) == 0:
            return 0
        x = x.split()

        return len(x)


if __name__ == '__main__':
    x = Solution()
    print(x.countSegments(", , , ,        a, eaefa"))