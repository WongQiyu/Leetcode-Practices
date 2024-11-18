# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# O(n) time and space
class Codec:
    def serialize(self, root):
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('')
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return
        data = data.split(",")
        ans = TreeNode(int(data[0]))
        q = deque([ans])
        i = 1
        while q:
            node = q.popleft()
            if i < len(data) and data[i]:
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1
            if i < len(data) and data[i]:
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i+= 1
        return ans


