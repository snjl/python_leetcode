class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0



if __name__ == '__main__':
    x = Solution()
    A = [2,1,2,7,8]
    print(x.largestPerimeter(A))