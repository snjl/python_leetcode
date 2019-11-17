class Solution:
    def getRow(self, numRows: int):
        if numRows == 0:
            return list([1])
        last_l = list()
        l = list()
        for i in range(1, numRows+2):
            l = [1 for _ in range(i)]
            # 表示第三层开始
            if i > 2:
                # 从该层的第1个数开始，len-2结束（len-1为最后一个元素）
                for j in range(1, len(l) - 1):
                    l[j] = last_l[j - 1] + last_l[j]
            last_l = l

        return l