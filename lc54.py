class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        r = len(matrix)
        c = len(matrix[0])
        res = []
        it, ib, jt, jb = 0, r-1, 0, c-1
    # R0 (1), c3(2), r2(1),c0(1), r(1)
        while it <= ib and jt <= jb:
            for j in range(jt, jb +1 ):
                res.append(matrix[it][j])
            it += 1
            for i in range(it,ib+1):
                res.append(matrix[i][jb])
            jb -= 1
            for j in range(jb,jt-1,-1):
                res.append(matrix[ib][j])
            ib -= 1
            for i in range(ib ,it-1,-1):
                res.append(matrix[i][jt])
            jt += 1
        return res[:r*c]
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder([[1, 2, 3,4], [5, 6,7,8], [9, 10, 11,12]]))
