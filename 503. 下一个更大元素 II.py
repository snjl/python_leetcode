class Solution:
    def nextGreaterElements(self, nums):
        result = [-1 for _ in nums]
        length = len(nums)

        nums = nums +nums
        # print(nums)
        s = list()
        for index in range(len(nums)):
            now_index = index % length

            if len(s) == 0 or s[-1][1] >= nums[index]:
                s.append((now_index,nums[index]))
            else:
                while len(s) > 0 and s[-1][1] < nums[index]:
                    i,_ = s.pop()
                    # print(now_index)
                    result[i] = nums[index]
                s.append((now_index,nums[index]))
        return result

if __name__ == '__main__':
    x = Solution()
    l = [1,2,1]
    print(x.nextGreaterElements(l))





