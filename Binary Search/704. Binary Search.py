from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # a = bisect_left(nums,target)
        # return a if a < len(nums) and nums[a] == target else -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

