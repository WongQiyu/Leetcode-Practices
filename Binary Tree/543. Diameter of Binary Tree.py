
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        def helper(root):
            nonlocal diameter
            left = helper(root.left) if root.left else 0
            right = helper(root.right) if root.right else 0
            if left + right > diameter:
                diameter = left + right
            return 1 + max(left, right)
        helper(root)
        return diameter

if __name__ == '__main__':
    #print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2), None)))
    print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))


