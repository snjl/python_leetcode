

def BucketSort(array,bucket_size=5):
    min_a = min(array)
    max_a = max(array)
    # 桶里有
    bucket_count = int((max_a - min_a) / bucket_size) + 1
    print(bucket_count)
    buckets = [list() for _ in range(bucket_count)]
    for i in array:
        index = int((i-min_a) / bucket_size)
        buckets[index].append(i)

    # 记录array的索引位置
    arr_i = 0
    for bucket in buckets:
        if len(bucket) != 0:
            # 对bucket内部进行排序
            bucket.sort()
            for i in bucket:
                array[arr_i] = i
                arr_i += 1

    return array

if __name__ == '__main__':
    array = [5, -1, 4, 3, 2, 7, 4, 6]

    BucketSort(array,2)
    print(array)
