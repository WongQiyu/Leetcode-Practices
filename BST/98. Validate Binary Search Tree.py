# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#[5,4,6,null,null,3,7]
import math
class Solution:
    def isValidBST(self, root):
        def helper(root, low, high):
            if not root:
                return True
            if low >= root.val or high <= root.val:
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        return helper(root, -math.inf, math.inf)
