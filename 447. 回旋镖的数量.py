from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points) -> int:
        count = 0
        for point in points:

            # distance2 记录对这个点来说的所有的距离
            distance2 = []
            for neighbor in points:
                distance2.append((point[0] - neighbor[0]) ** 2 + (point[1] - neighbor[1]) ** 2)

            frequency = Counter(distance2)

            for dist, num in frequency.items():
                if num >= 2:
                    count += num * (num - 1)

        return int(count)




if __name__ == '__main__':
    x = Solution()
    a = [[0,0],[1,0],[2,0]]
    print(x.numberOfBoomerangs(a))


