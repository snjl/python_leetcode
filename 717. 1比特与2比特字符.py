class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        # 统计紧接着0之前的1的个数，如果为奇数，则末尾必定是2比特，返回False，否则为1比特，返回True
        pre_num = 0
        if len(bits) < 2:
            return True
        if bits[-2] == 0:
            return True
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                pre_num += 1
            else:
                break
        if pre_num % 2 == 1:
            return False
        else:
            return True


if __name__ == '__main__':
    x = Solution()

    bits = [1, 0, 0]

    print(x.isOneBitCharacter(bits))
