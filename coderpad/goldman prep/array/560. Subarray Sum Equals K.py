class Solution:
    def subarraySum(self, nums, k):
        ans, pre_sum, d = 0, 0, {0:1}
        for num in nums:
            pre_sum += num
            if pre_sum - k in d:
                ans = ans + d[pre_sum - k]
            d[pre_sum] = d.get(pre_sum,0) + 1
            print(d)
        return ans


print(Solution().subarraySum([1,2,3],3))
#print(Solution().subarraySum([1],0))
#print(Solution().subarraySum([1],1))