from collections import deque
class Solution:
    def orangesRotting(self, grid):
        q = deque([])
        r = len(grid)
        c = len(grid[0])
        count, orange = 0, 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    orange += 1
        if orange == 0:
            return 0
        if not q and orange > 0:
            return - 1
        while q and orange > 0:
            i,j,count = q.popleft()
            for ni, nj in (i,j-1), (i, j+1), (i+1, j), (i-1,j):
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni,nj,count+1))
                    orange -= 1
        return count + 1 if orange == 0 else -1
if __name__ == '__main__':
    print(Solution().orangesRotting([[1,2]]))
    print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))