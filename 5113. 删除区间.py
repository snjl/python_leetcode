class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        t = list()
        for interval in intervals:

            # 移除部分的左界大于该部分左界
            if toBeRemoved[0] >= interval[1]:
                t.append(interval)
            # 移除部分的右界小于该部分右界
            elif toBeRemoved[1] <= interval[0]:
                t.append(interval)
            # 移除部分范围包含某个范围
            elif toBeRemoved[0] <= interval[0] and toBeRemoved[1] >= interval[1]:
                continue
            # 判断复杂情况
            elif toBeRemoved[0] >= interval[0] and toBeRemoved[1] >= interval[1]:
                t.append([interval[0], toBeRemoved[0]])
            elif toBeRemoved[0] <= interval[0] and toBeRemoved[1] <= interval[1]:
                t.append([toBeRemoved[1], interval[1]])
            elif toBeRemoved[0] >= interval[0] and toBeRemoved[1] <= interval[1]:
                t.append([interval[0], toBeRemoved[0]])
                t.append([toBeRemoved[1], interval[1]])

        return t

if __name__ == '__main__':

    x = Solution()
    # intervals = [[0, 2], [3, 4], [5, 7]]
    # toBeRemoved = [1, 6]
    intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]]
    toBeRemoved = [-1, 4]

    print(t)
