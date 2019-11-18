class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if len(nums) < 2:
            return False

        map = dict()
        flag = 0
        for i in range(len(nums)):
            if nums[i] in map.keys():
                abs_num = abs(i - map[nums[i]])
                # 如果有发现绝对值超过k的，则将当前位置存储到表中
                if abs_num > k:
                    map[nums[i]] = i
                if abs_num <= k:
                    flag = 1
                    break
                # elif abs_num > k:
                #     return False
                else:
                    continue
            else:
                map[nums[i]] = i
        if flag == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    x = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    # nums = [1,0,1,1]
    # k=1
    print(x.containsNearbyDuplicate(nums, k))
