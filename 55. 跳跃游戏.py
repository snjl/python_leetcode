class Solution:
    def canJump(self, nums) -> bool:
        jump_list = [False for _ in nums]
        jump_list[0] = True
        for i in range(len(nums)):
            for j in range(0, i):
                if jump_list[i] is True and i + nums[j] >= j:
                    jump_list[j] = True
                    break

        return jump_list[-1]


if __name__ == '__main__':
    x = Solution()

    print(x.canJump([3, 2, 1, 0, 4]))
