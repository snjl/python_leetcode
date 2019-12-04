class Solution:
    def pancakeSort(self, A):
        l = list()
        # 已经有序的部分
        already_sort = 0
        length = len(A)
        # 每2次交换确定一个有序数字，如果刚好有序数字在最前面，则第一次交换省去
        while self.if_sort(A[:length - already_sort]) is not True:
            max_index = A.index(max(A[:length - already_sort]))
            if max_index != 0:
                self.pancake(A, 0, max_index)
                l.append(max_index + 1)
            self.pancake(A, 0, length - already_sort - 1)
            l.append(length - already_sort)
            already_sort += 1
            print(A)
        return l

    def if_sort(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                return False
        return True

    # A的从i到j逆转
    def pancake(self, A, i, j):
        A[i:j + 1] = A[i:j + 1][::-1]


if __name__ == '__main__':
    A = [2, 1, 3, 4, 6, 5]
    A = [3, 2, 4, 1]
    x = Solution()
    print(x.pancakeSort(A))
