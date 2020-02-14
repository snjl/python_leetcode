import collections


class Solution:
    def pondSizes(self, land):
        if len(land) == 0:
            return list()
        l = list()
        height = len(land)
        width = len(land[0])
        for i in range(height):
            for j in range(width):
                if land[i][j] == 0:
                    self.bfs(i,j,l,height,width,land)

        l.sort()
        return l
    def bfs(self,i,j,l,height,width,land):
        count = 0
        q = collections.deque()
        q.appendleft((i,j))
        while len(q):
            x,y = q.pop()
            if 0<=x<height and 0<=y<width and land[x][y] == 0:
                land[x][y] = 1
                count += 1
                q.appendleft((x+1, y))
                q.appendleft((x-1, y))
                q.appendleft((x, y + 1))
                q.appendleft((x, y - 1))
                q.appendleft((x+1, y+1))
                q.appendleft((x+1, y-1))
                q.appendleft((x-1, y-1))
                q.appendleft((x-1, y+1))
        l.append(count)

if __name__ == '__main__':
    x= Solution()
    l = [
        [0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]
    ]
    print(x.pondSizes(l))
