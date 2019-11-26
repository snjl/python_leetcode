def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index],arr[i] =arr[i],arr[min_index]





if __name__ == '__main__':

    arr = [5, 1, 4, 3, 2, 7, 4, 6]

    SelectionSort(arr)
    print(arr)



