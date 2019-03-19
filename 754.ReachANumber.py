class Solution:
    def reachNumber(self, target: int) -> int:
        add_sum = 0
        step = 1
        target = abs(target)
        while target > add_sum:
            # 求出当前step时候add_sum的最大值
            add_sum = step * (step + 1) / 2
            if target == add_sum:
                return step
            step += 1
        # 将add_sum返回到比n小的状态，减去（step-1）的值（由于while里一直加1，直到n<=add_sum才跳出，实际上add_sum最后一个值是step-1
        step -= 1
        add_sum -= step
        # 返回step加到的真实情况
        step -= 1
        step += (target - add_sum) * 2
        return int(step)


if __name__ == '__main__':
    n = -1
    s = Solution()
    print(s.reachNumber(n))

    pass