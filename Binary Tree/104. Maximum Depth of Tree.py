# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([])
        q.append((root, 0))
        level = 0
        while q:
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return level + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def helper(node, level):
        #     if not node:
        #         return level
        #     left = helper(node.left, level + 1)
        #     right = helper(node.right, level + 1)
        #     return max(left, right) + 1
        # return helper(root,0)
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

