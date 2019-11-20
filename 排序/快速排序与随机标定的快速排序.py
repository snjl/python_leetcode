import random
import time

import sys

'''
快速排序与随机标定的快速排序
'''

# 解决递归层数问题
sys.setrecursionlimit(10000)


# 快速排序
def quick_sort(arr):
    new_L = arr.copy()
    return q_sort(new_L, 0, len(new_L) - 1)


# 随机标定的快速排序
def quick_sort_random(arr):
    new_L = arr.copy()
    return q_sort(new_L, 0, len(new_L) - 1)


def q_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)

        q_sort(arr, left, pivot - 1)
        q_sort(arr, pivot + 1, right)
    return arr


# 随机标定的快速排序
def q_sort_random(arr, left, right):
    if left < right:
        pivot = random_partition(arr, left, right)

        q_sort(arr, left, pivot - 1)
        q_sort(arr, pivot + 1, right)
    return arr


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


def random_partition(arr, left, right):
    i = random.randint(left, right)
    arr[i], arr[left] = arr[left], arr[i]
    return partition(arr, left, right)


# 参考：https://www.cnblogs.com/curtisxiao/p/11184773.html
def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [v for v in arr[1:] if v <= base]
        more = [v for v in arr[1:] if v > base]
        return quick_sort1(less) + [base] + quick_sort1(more)


if __name__ == '__main__':
    nums = [1, 2, 5, 4, 8, 9, 3, 6, 7]
    # nums = [3, 2, 1, 5, 6, -1, -2]
    nums = [5, 4, 2, 3, 7, 8]

    nums2 = [random.randint(0, 2) for _ in range(10000)]
    nums2 = [1 for i in range(40000, 0, -1)]
    start = time.time()
    x = quick_sort(nums2)
    print(x[:100])

    print(time.time() - start)
    start = time.time()
    x = quick_sort_random(nums2)
    print(x[:100])
    print(time.time() - start)
