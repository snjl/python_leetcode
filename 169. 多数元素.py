class Solution:
    def majorityElement(self, nums):
        d = dict()
        for n in nums:
            d[n] = d.get(n,0) + 1
            if d[n] * 2 > len(nums):
                return n
        return -1


if __name__ == '__main__':

    x = Solution()
    print(x.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))

