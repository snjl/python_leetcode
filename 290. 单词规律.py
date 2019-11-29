class Solution:
    def wordPattern(self, pattern, str) -> bool:
            s = str.split(' ')
            if len(s) != len(pattern):
                return False
            m = dict()
            for i in range(len(pattern)):
                # 如果某个字符未映射到s的该位置的字符串，则映射
                if pattern[i] not in m.keys():
                    if s[i] not in m.values():
                        # 如果s的该字符串也不在value中，才能添加，否则说明已经有对应的key，value了
                        m[pattern[i]] = s[i]
                    else:
                        return False
                # 如果映射到了，则比对原来映射的和现在映射的是否一样，如果不一样则False
                else:
                    if m[pattern[i]] != s[i]:
                        return False
            return True



