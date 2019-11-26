class Solution:
    def flipAndInvertImage(self, A):
        x = list()

        for line in A:
            line = line[::-1]
            line = [i^1 for i in line]
            x.append(line)
        return x



if __name__ == '__main__':
    x = Solution()

    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(x.flipAndInvertImage(A))