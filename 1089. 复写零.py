class Solution:
    # def duplicateZeros(self, arr) -> None:
    #     zero_count = 0
    #     # 原长度
    #     length = len(arr)
    #     # 不可再计算的长度，由于增加了0，后面的部分不会再算到，所以不再统计后面部分的0
    #     real_length = 0
    #     for i in range(length):
    #         if arr[i] == 0 and length - real_length >= i:
    #             zero_count += 1
    #             real_length += 1
    #
    #     # 真实可计算的部分从该位置开始
    #     real_calculate_index = length - real_length
    #     j = length - 1
    #     for i in range(real_calculate_index, -1, -1):
    #         if arr[i] != 0:
    #             arr[j] = arr[i]
    #             j -= 1
    #         else:
    #             arr[j] = 0
    #             j -= 1
    #             arr[j] = 0
    #             j -= 1

    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 1
            i += 1


if __name__ == '__main__':
    x = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    # arr = [1,2,3]
    # arr = [1,0,2]
    # arr = [0,]
    # arr = [0,1,7,6,0,2,0,7]
    x.duplicateZeros(arr)
    print(arr)