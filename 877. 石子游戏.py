class Solution:
    def stoneGame(self, piles) -> bool:
        piles.sort(reverse=True)
        # 先手
        a_sum = sum([piles[i] for i in range(len(piles)) if i%2 == 0])
        # 后手
        b_sum = sum([piles[i] for i in range(len(piles)) if i%2 == 1])

        return True if a_sum> b_sum else False




if __name__ == '__main__':
    x =Solution()
    piles = [5,3,4,5]


    print(x.stoneGame(piles))