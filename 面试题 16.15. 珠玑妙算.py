class Solution:
    def masterMind(self, solution: str, guess: str):
        guesses = list()
        real = dict()
        a = 0
        b = 0
        for i in range(len(solution)):
            if solution[i] == guess[i]:
                a += 1
            else:
                guesses.append(guess[i])
                real[solution[i]] = real.get(solution[i],0) + 1

        for i in guesses:
            if i in real.keys() and real[i] >= 1:
                real[i] -= 1
                b += 1

        return [a, b]



        pass