class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls_count = 0
        cows_map = dict()
        cows_count = 0
        lose_index = list()
        length = len(secret)
        for i in range(length):
            if secret[i] == guess[i]:
                bulls_count += 1
            else:
                cows_map[secret[i]] = cows_map.get(secret[i], 0) + 1
                lose_index.append(i)
        for i in lose_index:
            if cows_map.get(guess[i], 0) > 0:
                cows_count += 1
                cows_map[guess[i]] -= 1
        return str(bulls_count) + 'A' + str(cows_count) + 'B'
