class Solution:
    def findRelativeRanks(self, nums: list) -> list:
        m = dict()
        sort_nums = sorted(nums, reverse=True)

        # m存储已排序的每个数字的排名
        for index, num in enumerate(sort_nums):
            m[num] = index
        print()
        l = list()
        print(m)
        # 从原来的list中一个个去除,如果在m中该元素排序是第1、2、3则另外取值，否则取对应值+1的字符串
        for num in nums:
            if m[num] == 0:
                l.append("Gold Medal")
            elif m[num] == 1:
                l.append("Silver Medal")
            elif m[num] == 2:
                l.append("Bronze Medal")
            else:
                l.append(str(m[num] + 1))
        return l


if __name__ == '__main__':

    nums = [5,4,3,2,1]
    m = dict()
    sort_nums = sorted(nums,reverse=True)

    # m存储每个数字的位置
    for index, num in enumerate(sort_nums):
        m[num] = index
    print()
    l = list()
    print(m)

    for num in nums:
            if m[num] == 0:
                l.append("Gold Medal")
            elif m[num] == 1:
                l.append("Silver Medal")
            elif m[num] == 2:
                l.append("Bronze Medal")
            else:
                l.append(str(m[num] + 1))


    # for i in nums:
    #     if m[i] == 0:
    #         l.append("Gold Medal")
    #     elif m[i] == 1:
    #         l.append("Silver Medal")
    #     elif m[i] == 2:
    #         l.append("Bronze Medal")
    #     else:
    #         l.append(str(m[i]))
    print(l)
    pass
