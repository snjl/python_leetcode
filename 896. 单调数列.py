class Solution:
    def isMonotonic(self, A) -> bool:
        if len(A) <= 2:
            return True
        test_a = list()
        for i in range(len(A) - 1):
            test_a.append(A[i+1] - A[i])

        increase = False
        reduce = False
        for i in test_a:
            if i > 0:
                increase = True
            elif i<0:
                reduce = True
        if increase is True and reduce is True:
            return False
        else:
            return True



