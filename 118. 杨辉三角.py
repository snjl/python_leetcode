
class Solution:
    def generate(self, numRows: int) :
        if numRows == 0:
            return list()
        triangle = list()

        for i in range(1,numRows+1):
            l = [1 for _ in range(i)]
            # 表示第三层开始
            if i > 2:
                # 从该层的第1个数开始，len-2结束（len-1为最后一个元素）
                for j in range(1,len(l)-1):
                    l[j] = triangle[-1][j-1] + triangle[-1][j]
            triangle.append(l)

        return triangle

if __name__ == '__main__':
    x = Solution()

    numRows = 1
    numRows = 5

    print(x.generate(numRows))