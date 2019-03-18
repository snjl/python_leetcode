class Solution:
    def findErrorNums(self, nums: list) -> list:
        map = dict()
        nums_len = len(nums)
        for i in range(nums_len):
            map[i + 1] = 1
        same = None
        for index, i in enumerate(nums):
            if i in map.keys():
                map.pop(i)
            else:
                same = i
        real = None
        for i in map.keys():
            real = i
        return [same, real]
if __name__ == '__main__':
    nums = [2, 1, 3, 4,2, 6]
    s = Solution()
    print(s.findErrorNums(nums))
