from bisect import bisect, bisect_right, bisect_left
class Solution:
    def jobSchedulingSlow(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}
        def dfs(i):
            #base case if len(jobs) == 0 or to break
            if i == len(jobs):
                return 0
            if i in cache:
                return cache[i]
            # dont include
            res = dfs(i+1)
            #include
            # j = i + 1
            # while j < len(jobs):
            #     # 'proper', no overlap
            #     if jobs[i][1] <= jobs[j][0]:
            #         break
            #     j += 1
            # use bisect to prevent TLE
            j = bisect(jobs, (jobs[i][1], -1, -1))
            cache[i] = res= max(res, dfs(j) + jobs[i][2])
            return res
        return dfs(0)

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[1])
        print(jobs)
        dp = [[0, 0]]
        for s, e, p in jobs:
            #compare existing end time such that new start + 1 is "less than or equal to existing end time" --> no overlap
            i = bisect(dp, [s+ 1]) - 1
            print(i,dp,s+1)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
    # note that i need to bisect [] for [[]] even tho dp = [[0,0]] i can just bisect with [[0]]

if __name__ == '__main__':
    s = Solution()
    print(s.jobScheduling([1,2,3,3], [3,4,5,6],[50,10,40,70]))

'''
0 [[0, 0]] 2
0 [[0, 0], [3, 50]] 3
1 [[0, 0], [3, 50]] 4
1 [[0, 0], [3, 50], [5, 90]] 4
120
note bisect is same as bisect_right
rightmost insertion point
"[3,50] > 3" hence right most i is 1-1 = 0
'''