class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        # y =ax+b,y2-y1=a(x2-x1)
        if (coordinates[1][0] - coordinates[0][0]) ==0:
            a = 0
        else:
            a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i_xy in range(1, len(coordinates)):
            if (coordinates[i_xy][1] - coordinates[i_xy - 1][1]) != a * (
                    coordinates[i_xy][0] - coordinates[i_xy - 1][0]):
                return False
        return True


if __name__ == '__main__':
    x = Solution()

    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    coordinates = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]
    coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
    print(x.checkStraightLine(coordinates))
