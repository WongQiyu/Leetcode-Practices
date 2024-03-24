class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            res = target - val
            if res in d:
                return [d[res], i]
            d[val] = i
        return []