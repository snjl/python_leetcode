class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.strip().split(' ')[-1])



if __name__ == '__main__':
    x = Solution()

    s = 'a sdf'
    print(x.lengthOfLastWord(s))


