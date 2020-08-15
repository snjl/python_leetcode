# 参考： https://www.cnblogs.com/longyunfeigu/p/9316082.html

"""
二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；
其缺点是要求待查表为有序表，且插入删除困难。
因此，折半查找方法适用于不经常变动而查找频繁的有序列表。
首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，
如果两者相等，则查找成功；
否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，
则进一步查找前一子表，否则进一步查找后一子表。
重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。

"""

"""
1. 二分查找是有条件的，首先是有序，其次因为二分查找操作的是下标，所以要求是顺序表
2. 最优时间复杂度：O(1)
3. 最坏时间复杂度：O(logn)
"""


# 递归算法
def binary_search(lis, left, right, num):
    if left > right:  # 递归结束条件
        return -1
    mid = (left + right) // 2
    if num < lis[mid]:
        right = mid - 1
    elif num > lis[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search(lis, left, right, num)
    # 这里之所以会有return是因为必须要接收值，不然返回None
    # 回溯到最后一层的时候，如果没有return，那么将会返回None


# 非递归算法
def binary_search2(lis, num):
    left = 0
    right = len(lis) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找
            right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
        else:
            return mid  # 如果查询数字刚好为中间值，返回该值得索引
    return -1  # 如果循环结束，左边大于了右边，代表没有找到


if __name__ == '__main__':
    lis = [2, 4, 5, 12, 14, 23]
    # print(binary_search(lis, 0, len(lis) - 1, 4))
    print(binary_search2(lis, 5))
