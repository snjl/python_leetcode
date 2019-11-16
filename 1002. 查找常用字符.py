class Solution:
    def commonChars(self, A):
        a = list()
        len_A = [len(word) for word in A]
        # 找到字符串长度最短的下标
        min_len_index = len_A.index(min(len_A))
        min_word = A[min_len_index]
        exit_char = set()
        for c in min_word:
            if c in exit_char:
                continue
            exit_char.add(c)
            min_num = min_word.count(c)
            for word in A:
                if word.count(c) < min_num:
                    min_num = word.count(c)
            a.extend([c for _ in range(min_num)])
        return a


if __name__ == '__main__':
    x =Solution()
    A = ["bella", "label", "roller"]
    print(x.commonChars(A))