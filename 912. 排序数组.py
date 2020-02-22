# class Solution:
#     def sortArray(self,nums):
#         # 第一层for表示循环插入的遍数
#         for i in range(1, len(nums)):
#             for j in range(i, 0, -1):
#                 if nums[j] < nums[j - 1]:
#                     nums[j], nums[j - 1] = nums[j - 1], nums[j]
#                 else:
#                     break
#         return nums

class Solution:
    def sortArray(self,nums):

        # 普通快速排序
        def partition(arr, left, right):
            # 基准位置，所有元素都和基准比较
            pivot = left
            # index位置为开始排序的位置
            index = pivot + 1
            # 从index位置循环到最后一个位置（由于right存储的是数组长度-1，所以这里要+1才能到数组长度）
            for i in range(index, right + 1):
                # 如果比基准要小，i与index位置的元素交换值
                if arr[i] < arr[pivot]:
                    arr[i], arr[index] = arr[index], arr[i]
                    # 交换后，index位置上的值已经小于基准位置的值，所以移动到下一个位置，等待再次交换比基准更小的值
                    index += 1
            # 交换完成，index位置上的值大于基准位置，所以将基准位置与index-1位置的值交换
            # index-1的数值必定小于pivot位置数值，交换后，index-1为pivot数值，它之前的均为小于pivot数值的，之后的均为大于pivot数值的
            # index-1位置即成为分界线
            arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
            return index - 1

        def q_sort(arr, left, right):
            if left < right:
                pivot = partition(arr, left, right)

                q_sort(arr, left, pivot - 1)
                q_sort(arr, pivot + 1, right)
            return arr
        return q_sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':

    x = Solution()
    nums = [5,7,8,9,1,3,7]
    print(x.sortArray(nums))




