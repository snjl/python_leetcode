"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x * y


class Solution:
    def findSolution2(self, customfunction: 'CustomFunction', z: int):
        answers = list()
        for i in range(1,z + 1):
            for j in range(1,z + 1):
                z_ = customfunction.f(i,j)
                if z_ == z:
                    answers.append((i,j))
                    break
                elif z_ > z:
                    break

        return answers
    # 双指针法
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        ans, x, y = [], 1, z
        while x <= z and y >= 1:
            res = customfunction.f(x, y)
            if res < z:
                x += 1
            elif res > z:
                y -= 1
            if res == z:
                ans.append([x, y])
                x += 1
                y -= 1
        return ans



if __name__ == '__main__':
    x = Solution()
    print(x.findSolution(customfunction=CustomFunction(), z=5))