class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = 1
        is_odd = target % 2
        # 判断step到哪一步大于target（或者等于）
        while step * (step + 1) / 2 < target:
            step += 1
        # 等于时return step
        if step * (step + 1) / 2 == target:
            return step
        # 现在的step已经超过了target
        # target是奇数，判断step是不是除以4余几，余1或2均可，余3需要+2让其余1，余0需要+1让其余1
        if is_odd == 1:
            if step % 4 == 1 or step % 4 == 2:
                return step
            elif step % 4 == 3:
                return step + 2
            elif step % 4 == 0:
                return step + 1

        # target是偶数，判断step是不是除以4余几，余3或4均可，余2需要+1让其余3，余1需要+2让其余3
        else:
            if step % 4 == 3 or step % 4 == 0:
                return step
            elif step % 4 == 2:
                return step + 1
            elif step % 4 == 1:
                return step + 2
def get_next_set(l, num):
    next_set = set()
    for i in l:
        next_set.add(i - num)
        next_set.add(i + num)
    return next_set


if __name__ == '__main__':
    n = 12
    n = abs(n)
    l = set()
    l.add(0)
    for i in range(1, n):
        l = get_next_set(l, i)
        print(sorted(l))

    s = Solution()
    print(s.reachNumber(n))

    pass
