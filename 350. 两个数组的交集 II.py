class Solution:
    def intersect2(self, nums1, nums2):
        # 保证nums1是最短的，否则交换
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        same_list = list()
        for i in nums2:
            if len(nums1) > 0 and i in nums1:
                # 将i进行pop（index只会找到第一个数字为i的下标）
                same_list.append(nums1.pop(nums1.index(i)))
        return same_list

    def intersect(self,nums1,nums2):
        # 保证nums1是最短的，否则交换
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # 将list数据存入dict，空间换时间
        nums1_d = dict()
        for i in nums1:
            if nums1_d.get(i) is None:
                nums1_d[i] = 1
            else:
                nums1_d[i] += 1

        same_list = list()

        for i in nums2:
            if len(nums1_d) is not 0 and nums1_d.get(i) is not None:
                same_list.append(i)
                nums1_d[i] -= 1
                if nums1_d[i] == 0:
                    nums1_d.pop(i)
        return same_list

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 3, 4]
    a = s.intersect2(nums1, nums2)


