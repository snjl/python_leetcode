class Solution:
    def maxWidthRamp(self, A) -> int:
        stack = list()
        max_length = 0

        for i in range(len(A)):
            if len(stack) == 0:
                stack.append((i,A[i]))
            else:


                pass




        pass


if __name__ == '__main__':
    x = Solution()

    print(x.maxWidthRamp([6, 0, 8, 2, 1, 5]))
