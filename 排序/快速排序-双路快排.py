import random
import time

import sys

'''
快速排序-双路快排
参考：https://blog.csdn.net/m0_37519490/article/details/80648011
注意等号的解释：http://coding.imooc.com/learn/questiondetail/4920.html
'''


# 解决递归层数问题
sys.setrecursionlimit(10000)



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


# 随机标定的双路快排
def q_sort_random(arr, left, right):
    if left < right:
        pivot = random_partition(arr, left, right)

        q_sort(arr, left, pivot - 1)
        q_sort(arr, pivot + 1, right)
    return arr


# 普通双路快排
def partition(arr, left, right):
    # 基准位置，所有元素都和基准比较
    pivot = left

    # i，j分别为左右指针
    i, j = left + 1, right
    while True:
        # 当左指针未到右边，并且位置i的数小于基准位置，则继续记录i
        # 不能改为arr[i] <= arr[pivot]，否则可能导致不平衡
        # 可以改成i<=j，下面可以改为j>=i+1，但是因为实际上两者都无法到达right或left+1，因为i==j时，
        # arr[i]>arr[pivot]从而跳出循环，下一个循环同理
        while i <= right and arr[i] < arr[pivot]:
            i += 1
        # 当右指针未到左边，并且位置i的数小于基准位置，则继续记录j
        # 不能改为arr[j] >= arr[pivot]，否则可能导致不平衡
        while j >= left + 1 and arr[j] > arr[pivot]:
            j -= 1
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # 由于i,j均多走了一步，所以i>j，arr[j]>arr[pivot]，交换后即是以j为界
    # 例如[3, 2, 1, -2, -1, 6, 5]时，i,j=5,4，交换arr[j],arr[pivot]，
    # 变成[-1, 2, 1, -2, 3, 6, 5]，返回j的位置即可
    arr[j], arr[pivot] = arr[pivot], arr[j]

    return j



def random_partition(arr, left, right):
    i = random.randint(left, right)
    arr[i], arr[left] = arr[left], arr[i]
    return partition(arr, left, right)


if __name__ == '__main__':
    nums = [1, 2, 5, 4, 8, 9, 3, 6, 7]
    nums = [3, 2, 1, 5, 6, -1, -2]
    # nums = [5, 4, 2, 3, 7, 8]

    nums2 = [random.randint(0,2) for _ in range(10000)]
    # nums2 = [1 for i in range(40000,0,-1)]
    start = time.time()
    x = quick_sort(nums2)
    print(x[:100])

    print(time.time() - start)
    start = time.time()
    x = quick_sort_random(nums2)
    print(x[:100])
    print(time.time() - start)


    # print(quick_sort(nums))