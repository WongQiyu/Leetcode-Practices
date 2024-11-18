class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(nums, low, high):
            mid = (low + high) // 2
            while low < high:
                if nums[high] < nums[mid]:
                    return helper(nums, mid + 1, high)
                else:
                    return helper(nums, 0, mid)
            return nums[mid]

        return helper(nums, 0, len(nums) - 1)

