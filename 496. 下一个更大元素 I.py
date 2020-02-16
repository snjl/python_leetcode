class Solution:
    def nextGreaterElement1(self, nums1, nums2):
        m = dict()
        nums2_len = len(nums2)
        for index, num in enumerate(nums2):
            m[num] = index
        result = list()
        for i in nums1:
            index = m[i]
            # 是否找到更大的值
            flag = False
            for next_num_index in range(index,nums2_len):
                if nums2[next_num_index] > i:
                    result.append(nums2[next_num_index])
                    flag = True
                    break
            if flag is False:
                result.append(-1)
        return result

    def nextGreaterElement(self, nums1, nums2):
        stack = list()

if __name__ == '__main__':
    x = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(x.nextGreaterElement(nums1, nums2))
