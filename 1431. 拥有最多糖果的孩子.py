class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret
