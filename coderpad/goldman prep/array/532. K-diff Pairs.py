from collections import Counter
class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            d = Counter(nums)
            count = 0
            for v in d.values():
                if v >= 2: count+= 1
            return count
        check = set(nums)
        count = 0
        for i in check:
            if i + k in check:
                count+= 1

        return count

print(Solution().findPairs([1,3,1,5,4],0))