class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0,0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0,0) or (dx, dy) != (0, 1)
#https://leetcode.com/problems/robot-bounded-in-circle/solutions/290856/java-c-python-let-chopper-help-explain/
        '''
        N (0,1)
        E (1,0)
        S (0,-1)
        W (-1,0)
        N>E>S>W : right dx, dy = dy, -dx
        left dx, dy = -dy, dx
        if chopper return to the origin, he is obvious in an circle.
    if chopper finishes with face not towards north,
    it will get back to the initial status in another one or three sequences. 
[[0,1],[-1,0] ]--> right 90 degree clockwise
[[0,1],[-1,0] ][dx,dy] = [dy,-dx]
        '''
