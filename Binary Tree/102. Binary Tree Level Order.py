from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        q = deque([])
        if not root:
            return []
        res, curr = [[]], 0
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if level > curr:
                curr += 1
                res.append([])
            res[-1].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        return res
if __name__ == '__main__':
    print(Solution().levelOrder(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None,None),TreeNode(7 , None,None) ))))


