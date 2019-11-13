class Solution:
    def game(self, guess, answer) -> int:
        correct = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                correct += 1

        return correct


if __name__ == '__main__':
    x = Solution()
    guess = [1,2,3]
    answer = [1,2,3]

    print(x.game(guess,answer))
