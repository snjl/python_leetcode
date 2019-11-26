class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        max_num = -1
        max_index = -1
        for i in range(len(A)):
            if A[i]>max_num:
                max_index = i
                max_num = A[i]
            else:
                break
        return max_index