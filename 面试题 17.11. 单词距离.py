class Solution:
    def findClosest(self, words, word1: str, word2: str) -> int:
        count1 = list()
        count2 = list()
        for i, word in enumerate(words):

            if word == word1:
                count1.append(i)
            elif word == word2:
                count2.append(i)

        min_dis = len(words)
        cur1 = 0
        cur2 = 0

        while cur1 < len(count1) and cur2 < len(count2):
            dis = count1[cur1] - count2[cur2]
            if dis > 0:
                min_dis = min(min_dis, dis)
                cur2 += 1
            else:
                min_dis = min(min_dis, abs(dis))
                cur1 += 1

        return min_dis


if __name__ == '__main__':
    words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
    word1 = "a"
    word2 = "student"
    x = Solution()
    print(x.findClosest(words, word1, word2))
