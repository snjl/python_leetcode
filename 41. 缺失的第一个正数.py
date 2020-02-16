class Solution:
    def firstMissingPositive(self, nums) -> int:
        l = len(nums)
        if l == 0:
            return 1
        for i in range(1, l + 1):
            if i not in nums:
                return i
        return l + 1

if __name__ == '__main__':
    x = Solution()
    l = [1, 2, 3]
    print(x.firstMissingPositive(l))
