class Solution:
    def findErrorNums(self, nums):
        same = 0
        lost = 0
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                same = num

        for i in range(len(nums)):
            if i+1 not in s:
                lost = i + 1
                break
        return [same,lost]



if __name__ == '__main__':
    nums = [3,3,1]
    x = Solution()
    print(x.findErrorNums(nums))






