from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        if x == y:
            return False
        res = [0,0]
        q = deque([(0, root,0)])
        x_lvl,  x_parent = 0, 0
        y_lvl,  y_parent = 0, 0
        while q:
            lvl, curr, parent = q.popleft()
            if res == [1,1]:
                break
            if curr.val == x:
                x_lvl = lvl
                x_parent = parent
                res[0] = 1
            if curr.val == y:
                y_lvl = lvl
                y_parent = parent
                res[1] = 1
            if curr.left:
                q.append((lvl+1, curr.left,curr))
            if curr.right:
                q.append((lvl + 1, curr.right, curr))

        return True if x_lvl == y_lvl and x_parent != y_parent else False