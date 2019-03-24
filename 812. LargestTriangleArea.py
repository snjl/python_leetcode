class Solution:
    def largestTriangleArea(self, points: list):
        area = 0
        size = len(points)
        for i in range(size):
            for j in range(i + 1,size):
                for k in range(j + 1,size):
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    x3 = points[k][0]
                    y3 = points[k][1]
                    new_area = self.get_area(x1,y1,x2,y2,x3,y3)
                    if new_area > area:
                        area = new_area
        return area

    def get_area(self,x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

if __name__ == '__main__':
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    s = Solution()
    print(s.largestTriangleArea(points))