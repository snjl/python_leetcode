

def CountingSort(nums):
    min_n = min(nums)
    max_n = max(nums)
    # 开辟一块新的空间创建新的数组，位置0实际代表min_n+0，位置x代表min_n+x，位置上的值t代表原数组中有t个该值
    bucket_nums = [0 for _ in range(min_n,max_n+1)]

    for i in nums:
        bucket_nums[i - min_n] += 1
    print(bucket_nums)

    # 从计数bucket中拿数据的位置i
    bucket_i = 0
    for i in range(len(nums)):
        while bucket_nums[bucket_i] != 0:
            nums[i] = bucket_i + min_n
            bucket_nums[bucket_i] -= 1
            # 如果该位置拿完了数，往后拿
            if bucket_nums[bucket_i] == 0:
                bucket_i += 1
            break

    return nums


if __name__ == '__main__':
    x = [5, 1, 4, 3, 2, 7, 4, 6]

    CountingSort(x)
    print(x)
