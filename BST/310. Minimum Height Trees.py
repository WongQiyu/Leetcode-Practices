from collections import defaultdict

class Solution:
    def findMinHeightTrees(n, edges):
        al = [[] for _ in range(n)]
        for u,v in edges:
            al[u].append(v)
            al[v].append(u)