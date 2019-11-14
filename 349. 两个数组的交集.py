
class Solution:
    def intersection2(self, nums1, nums2):
        return list(set(nums1)&set(nums2))

    def intersection(self, nums1, nums2):
        l = list()
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                l.append(i)
        return l
