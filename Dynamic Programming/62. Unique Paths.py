class Solution:
    def uniquePaths(self, m, n):
        # if one row, only one path, draw on excel to visualize
        dp = [1] * n
        for _ in range(1,m):
            for i in range(n-2,-1,-1):
                dp[i] += dp[i+1]
        return dp[0]

    # dp = [1] * n
    # for _ in range(1, m):
    #     for i in range(1, n):
    #         dp[i] += dp[i - 1]
    # return dp[-1]





if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(13, 4))