import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = math.inf
        max_diff = 0
        for item in prices:
            diff = item - min_val
            if diff > max_diff:
                max_diff = diff
            if item < min_val:
                min_val = item
        return max_diff