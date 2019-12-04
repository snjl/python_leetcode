class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        num = 0
        # 让Y接近X，Y的操作为除以2和加1，如果X>Y了，说明X需要递减操作
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                num += 1
            else:
                Y //= 2
                num += 1
        num += (X - Y)
        return num


if __name__ == '__main__':
    x= Solution()

    X = 2
    Y = 3


    print(x.brokenCalc(X,Y))