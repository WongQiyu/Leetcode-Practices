class Solution:
    def pivotIndex(self, nums):
        ls, rs = 0, sum(nums)
        for i, ele in enumerate(nums):
            rs -= ele
            if ls == rs:
                return i
            ls += ele
        return -1
print(Solution().pivotIndex([1,7,3,6,5,6]))