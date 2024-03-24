from collections import deque
from heapq import heapify, heappush, heappop
impor
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#[3,1,4,null,2]
class Solution:
    def kthSmallest(self, root, k):
        store = []
        heapify(store)
        q = deque([(root.val, root)])
        while q:
            val, node = q.popleft()
            heappush(store, (-val, node))
            if node.left:
                q.append((node.left.val, node.left))
            while len(store) > k:
                heappop(store)
            if len(store) < k and node.right:
                q.append((node.right.val, node.right))
            if len(store) == k and node.right:
                tmp, tmp_node = heappop(store)
                if node.right.val < -tmp:
                    q.append((node.right.val, node.right))
                heappush(store, (tmp, tmp_node))

        return -heappop(store)[0]
