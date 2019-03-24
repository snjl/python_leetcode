class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        all_S = sum(A)
        if all_S % 3 != 0:
            return False

        S_1 = 0
        break_1 = 0
        S_2 = 0

        for index, num in enumerate(A):
            S_1 += num
            print(S_1)
            if S_1 == all_S / 3:
                break_1 = index
                break
        for index, num in enumerate(A[break_1 + 1:]):
            S_2 += num
            if S_2 == all_S / 3:
                break
        if S_1 == S_2 and S_1 == all_S / 3:
            return True
        else:
            return False

if __name__ == '__main__':
    A = [6,1,1,13,-1,0,-10,20]
    s = Solution()
    print(s.canThreePartsEqualSum(A))