def merge(a, b):
    c = []
    h = j = 0
    # 比较左右两个数组各自的大小
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    # 整数除法
    middle = len(arr) // 2
    # 左右分开后调用mergeSort，返回左右合并后的merge
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left, right)





if __name__ == '__main__':

    arr = [5, 1, 4, 3, 2, 7, 4, 6]

    b = mergeSort(arr)
    print(b)
