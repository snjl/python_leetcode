class Solution:
    def calculate(self, s: str) -> int:
        nums = list()
        stack = list()
        import re
        s = re.sub('([*+-/])', r' \1 ', s.replace(' ', '')).split()

        for i in s:
            # 如果是符号，压入stack
            if i in ['+', '-', '*', '/']:
                if i in ['*', '/']:
                    # 如果是乘除号，压入
                    stack.append(i)
                # 如果是加号
                else:
                    # 判断上一个是不是乘除，是的话pop nums进行乘除，然后压入符号和数字
                    if len(stack) > 0 and stack[-1] in ['*', '/']:
                        last = stack.pop()
                        n1 = nums.pop()
                        n2 = nums.pop()
                        if last == '*':
                            nums.append(n1 * n2)
                        else:
                            nums.append(n2 // n1)
                        stack.append(i)
                    else:
                        stack.append(i)
            else:
                nums.append(int(i))
        #     print(nums,stack)
        #
        # print('---')
        # print(stack, nums)
        while len(stack):
            k = stack.pop()
            n1 = nums.pop()
            n2 = nums.pop()
            if k == '+':
                nums.append(n1 + n2)
            elif k == '-':
                nums.append(n2 - n1)
            elif k == '*':
                nums.append(n1 * n2)
            else:
                nums.append(n2 // n1)

        return nums[0]


if __name__ == '__main__':
    x = Solution()

    print(x.calculate("1-1+1"))
