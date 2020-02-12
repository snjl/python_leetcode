class Solution:
    def heightChecker(self, heights) -> int:
        sorted_heights = heights[::]
        sorted_heights.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
