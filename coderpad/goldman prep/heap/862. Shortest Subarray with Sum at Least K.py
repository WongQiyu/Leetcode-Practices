from collections import deque
import math
class Solution:
    def shortestSubarray(self, nums, k):
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        q = deque([])
        res = float(math.inf)

        for i, total in enumerate(pre):
            while (q and q[-1][-1] >= total):
                q.pop()

            while (q and total - q[0][1] >=k):
                res = min(i-q[0][0],res)
                q.popleft()
            q.append([i, total])

        return res if res != float('inf') else -1