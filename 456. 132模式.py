class Solution:


    # 没做出来
    def find132pattern2(self, nums) -> bool:
        stack = list()
        for i in nums:
            if len(stack) == 0 or stack[-1] <= i:
                stack.append(i)
            else:
                print(stack,i)
                while len(stack) > 0 and stack[-1] > i:
                    stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    return True
        return False


if __name__ == '__main__':
    x = Solution()
    l = [3, 5, 0, 3, 4]
    print(x.find132pattern(l))
