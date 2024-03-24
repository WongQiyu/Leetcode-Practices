class Solution:
    def sortColors(self, nums):
        l,r,index = 0, len(nums) -1, 0
        while index <= r:
            if nums[index] == 2:
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1
            elif nums[index] == 0:
                nums[index], nums[l] = nums[l], nums[index]
                l+= 1
                index += 1
            else:
                index += 1
        return nums
