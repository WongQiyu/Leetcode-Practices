class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        if sx == tx:
            return (ty-sy) %sx == 0 # only change y
        if sy == ty:
            return (tx-sx) %sy == 0
        if tx > ty:
            return self.reachingPoints(sx, sy, tx %ty, ty)
        elif tx < ty:
            return self.reachingPoints(sx, sy, tx, ty %tx)
        else:
            False
        # (1,1) --> (1,2) --> (1,3)
        '''
        Work backwards. Greatest common divisior
        3,5
        /\/\
        3   2
        /\
        1 2
        1 1

        (1,1) --> (1,2) --> (3,2) -->(3,5)
         
        (3, 10) --> (3, 7) --> (3,4) -- > (3,1) --> (2,1)
        10 % 3 = 1
        (3,1) --> (3,1) --> (2,1)
        
         (1,1)
        
        O(log(min(tx,ty))) time and space
        euclidean algo for GCD. reduce size logaritm
        '''