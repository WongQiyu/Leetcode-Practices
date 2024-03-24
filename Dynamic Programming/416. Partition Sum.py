class Solution:
    def canPartition(self, nums):
        dp = {0}
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        for item in nums:
            if item == half:
                return True
            elif item > half:
                return False
            next_dp = set()
            for t in dp:
                val = t + item
                if val == half:
                    return True
                if val < half:
                    next_dp.add(t + item)
                next_dp.add(t)
            dp = next_dp
        return False
# s>>1 halfs the value, s&1 is an odd number
if __name__ == '__main__':
    #print(Solution().canPartition([1, 5, 11, 5]))
    #print(Solution().canPartition([1, 2, 3, 5]))
    print(Solution().canPartition([3, 3, 3, 4, 5]))
