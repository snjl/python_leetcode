class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for j in range(len(s)):
            end_flag = 0
            l = set()

            for i in range(j, len(s)):
                if s[i] not in l:
                    l.add(s[i])
                    # 到最后一个位置了
                    if i == len(s) - 1:
                        end_flag = 1
                    # print(l)
                    max_len = max(max_len, len(l))
                else:
                    l.clear()
                    break

            # 表示到达了最后位置，不可能有比这个更大了，提前break
            if end_flag == 1:
                break
        return max_len


