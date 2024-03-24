from math import inf
class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) -1
        max_area = -inf
        l = 0
        while l != r:
            height_l, height_r = height[l], height[r]
            if height_l <= height[r]:
                l += 1
                h = height_l
            else:
                r -= 1
                h = height_r
            # rmb + 1 cos our new l and r is diff
            max_area = max(h * (1+(r-l)), max_area)
        return max_area