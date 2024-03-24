class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        row = len(image)
        col = len(image[0])
        vis = [[0 for i in range(col)] for j in range(row)]

        def dfs(i, j):
            if image[i][j] == og:
                image[i][j] = color
                vis[i][j] = 1
                for ni, nj in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= ni < row and 0 <= nj < col and vis[ni][nj] == 0:
                        dfs(ni, nj)

        dfs(sr, sc)
        return image
