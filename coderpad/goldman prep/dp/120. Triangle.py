class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for lst in triangle[1:]:
            check = len(lst) - 2
            curr = [0] * len(lst)
            for j, v in enumerate(lst):
                if j - 1 < 0:
                    curr[j] = v + prev[j]
                elif j > check:
                    curr[j] = v + prev[j - 1]
                else:
                    curr[j] = min(prev[j] + v, prev[j - 1] + v)
            prev = curr
        return min(prev)
