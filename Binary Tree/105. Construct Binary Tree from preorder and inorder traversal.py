class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeOld(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = preorder[0]
        i = inorder.index(root)
        result = TreeNode(root)
        result.left = self.buildTreeOld(preorder[1:i + 1], inorder[:i])
        result.right = self.buildTreeOld(preorder[i + 1:], inorder[i + 1:])
        return result

    def buildTree(self, preorder, inorder):
        preorder.reverse()
        inorder_dict = {v:i for i,v in enumerate(inorder)}

        def helper(preorder, inorder_dict, beg, end):
            if beg > end:
                return None
            root = TreeNode(preorder.pop())
            i = inorder_dict[root.val]
            root.left = helper(preorder, inorder_dict, beg, i - 1)
            root.right = helper(preorder, inorder_dict, i + 1, end)
            return root
        return helper(preorder, inorder_dict, 0, len(preorder) - 1)
