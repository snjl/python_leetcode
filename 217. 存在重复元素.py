class Solution:
    def containsDuplicate1(self, nums) -> bool:
        return not len(nums) == len(set(nums))

    def containsDuplicate(self, nums) -> bool:
        d = dict()
        for i in nums:
            if i in d.keys():
                return True
            else:
                d[i] = 0

        return False


if __name__ == '__main__':
    s = Solution()
    x = [2, 2, 2, 3, 3, 4, 4]
    a = s.containsDuplicate(x)
    print(a)
