# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        l = 0
        for i in range(len(points) - 1):
            x = abs(points[i + 1][0] - points[i][0])
            y = abs(points[i + 1][1] - points[i][1])

            path_length = max(x, y)
            l += path_length
            # print(points[i], points[i + 1],path_length)

        return l


if __name__ == '__main__':
    x = Solution()
    points = [[559, 511],[-35, -852], [25, -495], [185, 671], [149, -452]]
    # points = [[1,1],[3,4],[-1,2]]
    print(x.minTimeToVisitAllPoints(points))
