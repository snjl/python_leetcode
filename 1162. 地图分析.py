class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        vst = {(i, j) for j in range(n) for i in range(n) if grid[i][j]}  # 访问点初始化
        if not 0 < len(vst) < n * n:  # 如果全海或全陆就返回-1
            return -1
        que = vst.copy()  # 队列初始化
        ans = 0  # 步长初始化
        while len(vst) < n * n:  # 未访问所有点时继续宽搜
            tmp = set()
            for i, j in que:  # 宽搜扩展
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and (x, y) not in vst:
                        tmp.add((x, y))
                        vst.add((x, y))
            ans += 1
            que = tmp
        return ans


if __name__ == '__main__':
    x = Solution()

    l = [[1,0,1],[0,0,0],[1,0,1]]
    print(x.maxDistance(l))
