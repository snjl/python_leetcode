class Solution:
    def missingNumber(self, nums) -> int:
        m = dict()
        for i in nums:
            m[i] = 1

        for i in range(0,len(nums) + 1):
            if m.get(i,-1) == -1:
                return i
        return -1

        pass

if __name__ == '__main__':
    x = Solution()

    print(x.missingNumber([3,0,1]))

