class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                tmp = min(grid[i-1][j],grid[i][j-1])
                grid[i][j] += tmp
        return grid[-1][-1]