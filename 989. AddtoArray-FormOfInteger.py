class Solution1:
    def addToArrayForm(self, A: list, K: int) -> list:
        K = self.int_to_list(K)
        l = max(len(A), len(K))
        A = self.extend_zero(A, l)
        K = self.extend_zero(K, l)
        # print(m)
        # print(n)
        nums = list()
        for i in range(l):
            nums.append(A[i] + K[i])
        # print('nums:', nums)
        new_nums = list()
        add = 0
        while len(nums) != 0:
            num = nums.pop()
            # 求出原位与进位
            now = num + add
            stay = now % 10
            add = int(now / 10)
            new_nums.append(stay)
            if len(nums) == 0 and add == 1:
                new_nums.append(1)
        new_nums.reverse()
        return new_nums

    def int_to_list(self, num):
        l = list()
        while num != 0:
            l.append(num % 10)
            num = int(num / 10)
        l.reverse()
        return l

    def extend_zero(self, l, length):
        while len(l) < length:
            # l前面补0
            b = [0]
            b.extend(l)
            l = b
        return l


class Solution:
    def addToArrayForm(self, A, K):
        i = len(A) - 1

        A[-1] = A[-1] + K

        while i > 0 and A[i] > 9:
            A[i - 1] = A[i - 1] + A[i] // 10
            A[i] = A[i] % 10
            i = i - 1

        while A[0] > 9:
            A.insert(0, A[0] // 10)
            A[1] = A[1] % 10
        return A

def int_to_list( num):
    l = list()
    while num != 0:
        l.append(num % 10)
        num = int(num / 10)
    l.reverse()
    return l



def form(l):
    length = len(l)
    l.reverse()


if __name__ == '__main__':
    m = 9999
    s = Solution()
    m = int_to_list(m)
    n = [1]

    l = max(len(m),len(n))
    m = extend_zero(m,l)
    n = extend_zero(n,l)
    print(m)
    print(n)
    nums = list()
    for i in range(l):
        nums.append(m[i] + n[i])
    print('nums:',nums)
    new_nums = list()
    add = 0
    while len(nums) != 0:
        num = nums.pop()
        # 求出原位与进位
        now = num + add
        stay = now % 10
        add = int(now / 10)
        new_nums.append(stay)
        if len(nums) == 0 and add == 1:
            new_nums.append(1)
    new_nums.reverse()
    print(new_nums)


    # print(s.addToArrayForm(n,m))
