class Solution:
    def findSpecialInteger(self, arr) -> int:
        count_num = int(len(arr) / 4)

        for i in range(len(arr) - count_num):
            if arr[i] == arr[i + count_num]:
                return arr[i]





        pass




if __name__ == '__main__':
    x =Solution()
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(x.findSpecialInteger(arr))


