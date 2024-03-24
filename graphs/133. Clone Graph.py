from collections import deque
# Definition for a Node.
'''
DFS : resturn dfs(node)
create visited dict
create a new node Node(node.val), ignore neighbor first
make node.val the key and node = Node(node.val) the value
if else:
if not in visited: new.append(dfs(neigh))
else: new.append(visited[neigh].val)

bfs: make node the key and vis[node] = Node(node.val,[])
subsequently add neighnor to queue
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque([node])
        visited= {node: Node(node.val, [])}
        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val,[])
                    q.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
    def cloneGraphdfs(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if not node:
                return None
            new = Node(node.val)
            visited[node.val] = new
            for adj in node.neighbors:
                if adj.val not in visited:
                    new.neighbors.append(dfs(adj))
                else:
                    new.neighbors.append(visited[adj.val])
            return new
        return dfs(node)

    def cloneGraphdfs2(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if not node:
                return None
            visited[node] = Node(node.val,[])
            for adj in node.neighbors:
                if adj not in visited:
                    visited[node].neighbors.append(dfs(adj))
                else:
                    visited[node].neighbors.append(visited[adj])
            return visited[node]

        return dfs(node)
        # mapping = {node: Node(node.val,[])}
        # queue = deque([node])
        # while queue:
        #     curr_node = queue.popleft()

