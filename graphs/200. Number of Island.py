class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            #check[i][j] = True
            grid[i][j] = 0
            for ni, nj in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                #if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == '1' and not check[ni][nj]:
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == '1':
                    dfs(ni, nj)

        r = len(grid)
        c = len(grid[0])
       # check = [[False for _ in range(c)] for _ in range(r)]
        count = 0
        for a in range(r):
            for b in range(c):
                #if grid[a][b] == '1' and not check[a][b]:
                if grid[a][b] == '1':
                    dfs(a, b)
                    count += 1

        return count
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
            count = 0
            for r,row in enumerate(grid):
                for c,col in enumerate(row):
                    if grid[r][c] == '1':
                        self.removeNeighbors(r,c,grid)
                        count += 1
            return count
    def removeNeighbors(self, r ,c, grid):
        grid[r][c] = 0
        if r+1 < len(grid) and grid[r+1][c] == '1':
            self.removeNeighbors(r+1,c,grid)
        if c+1 < len(grid[0]) and grid[r][c+1] == '1':
            self.removeNeighbors(r,c+1,grid)
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.removeNeighbors(r-1,c,grid)
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.removeNeighbors(r,c-1,grid)
if __name__ == '__main__':
    print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

