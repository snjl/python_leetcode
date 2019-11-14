from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        max_time = 0
        res = ''
        for ht,  hb, mt, mb in permutations(A):
            hour, minute = ht * 10 + hb, mt * 10 + mb
            t = hour * 60 + minute
            if hour < 24 and minute < 60 and t >= max_time:
                res = "{}{}:{}{}".format(ht, hb, mt, mb)
                max_time = t
        return res




if __name__ == '__main__':
    x = Solution()

    A = [1,2,3,4]
    # A=[5,5,5,5]
    # A=[2,3,4,5]
    # A= [0,0,0,0]
    # A = [4,2,4,4]
    # A = [2,0,6,6]
    print(x.largestTimeFromDigits(A))


