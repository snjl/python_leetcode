def BubbleSort(arr):
    # i表示已有多少元素排好序
    for i in range(0, len(arr) - 1):
        # j表示从0到len(arr)-i重新排序，由于内部有j+1，所以循环时要-1
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


# 改进版
def BubbleSort2(arr):
    # i表示已有多少元素排好序
    for i in range(0, len(arr) - 1):
        # 设定一个标记，若为true，则表示此次循环没有进行交换，也就是待排序列已经有序，排序已经完成
        flag = True
        # j表示从0到len(arr)-i重新排序，由于内部有j+1，所以循环时要-1
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = False
        if flag:
            break


if __name__ == '__main__':
    x = [5, 1, 4, 3, 2, 7, 4, 6]

    BubbleSort2(x)
    print(x)
