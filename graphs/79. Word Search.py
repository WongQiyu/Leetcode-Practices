class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j, word, index, board):
            if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != word[index]:
                return False
            if index== len(word) -1:
                return True
            board[i][j] = -1
            for ni, nj in ((i,j +1), (i ,j-1), (i-1,j), (i+1,j)):
                if dfs(ni,nj,word, index+1,board):
                    return True
            board[i][j] = word[index]
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if dfs(i,j,word,0, board):
                    return True
        return False





