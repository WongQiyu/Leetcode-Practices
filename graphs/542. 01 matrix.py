from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        rows = len(mat)
        cols= len(mat[0])
        # interesting to note below furthest_zero
        furthest_zero = max(rows,cols)
        q = deque()
        dir = ((0,1), (0,-1), (1,0), (-1,0))
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = furthest_zero
        while q:
            i,j = q.popleft()
            for ni, nj in dir:
                ni, nj = ni + i, nj + j
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] > mat[i][j]:
                    q.append((ni,nj))
                    mat[ni][nj] = mat[i][j] + 1
        return mat
