class Solution:
    def singleNumber(self, nums) -> int:
        d = {}
        for i in nums:
            if d.get(i) is not None:
                d.pop(i)
            else:
                d[i] = 1
        return d.popitem()[0]

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a



if __name__ == '__main__':
    s = Solution()
    a = s.singleNumber([1,2,2,3,3])
    print(a)
