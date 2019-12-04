class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        d1 = 0
        if start > destination:
            destination, start = start, destination
        for i in range(start, destination):
            d1 += distance[i]
        d2 = sum(distance) - d1
        return min(d1, d2)


if __name__ == '__main__':
    x = Solution()

    distance = [1, 2, 3, 4]
    start = 0
    destination = 3

    print(x.distanceBetweenBusStops(distance, start, destination))
