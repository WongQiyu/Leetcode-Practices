from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = deque([])
        q.append((root, 0))
        level, check_len, check_len_next, res = 0, 1, 0, []
        while q:
            node, level = q.popleft()
            check_len -= 1
            if node.left:
                q.append((node.left, level + 1))
                check_len_next += 1
            if node.right:
                q.append((node.right, level + 1))
                check_len_next += 1
            if check_len == 0:
                res.append(node.val)
                check_len, check_len_next = check_len_next, 0
        return res

    def rightSideView2(self, root):
        res = []
        d = 0
        def rs(root, res, d):
            if not root:
                return
            if len(res) == d:
                res.append(root.val)
            d += 1
            rs(root.right, res, d)
            rs(root.left, res, d)
        rs(root, res, d)
        return res
