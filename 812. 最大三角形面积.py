import math


class Solution:
    def largestTriangleArea(self, points):
        m = -1
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    if i != j and i != k and j != k:
                        m = max(m, self.calculate_area(points[i], points[j], points[k]))
        return m

    def calculate_area(self, point1, point2, point3):
        r1 = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        r2 = math.sqrt((point1[0] - point3[0]) ** 2 + (point1[1] - point3[1]) ** 2)
        r3 = math.sqrt((point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2)
        p = (r1+r2+r3)/2
        area = math.sqrt(abs(p* (p-r1) *(p- r2) *(p- r3)))
        return area


if __name__ == '__main__':
    x = Solution()
    a = [[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]
    print(x.largestTriangleArea(a))
