def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


if __name__ == '__main__':

    arr = [4, 3, 2, 1, 6, 7, 5, 4, 9, 3]
    # 默认第一个有序，所以从位置1开始，将每一个数插入到有序的数组中
    for i in range(1, len(arr)):
        # temp保留arr[i]，j保留位置i
        temp = arr[i]
        j = i
        # 如果j未到位置0，并且temp比arr[j-1]小，说明排序位置在前面，如果arr[j-1]比temp大或者j=0了（也是到最小的位置了），则停下
        while j > 0 and temp < arr[j - 1]:
            # 将位置j-1的数据填入位置j
            arr[j] = arr[j-1]
            j -= 1
        # j<i表示arr[j]的位置已经空出来，temp值比arr[j]后面的值都小，插入
        if j < i:
            arr[j] = temp

    print(arr)
