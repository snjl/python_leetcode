class Solution:
    # 会超时
    def canJump2(self, nums) -> bool:
        jump_list = [False for _ in nums]
        jump_list[0] = True
        for i in range(len(nums)):
            for j in range(0, i):
                if jump_list[i] is True and i + nums[j] >= j:
                    jump_list[j] = True
                    break

        return jump_list[-1]

    def canJump(self, nums) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

if __name__ == '__main__':
    x = Solution()

    print(x.canJump2([3, 2, 1, 0, 4]))
