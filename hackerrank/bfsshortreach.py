#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def bfs(n, m, edges, s):
    AL = [[] for _ in range(n)]
    for a,b in edges:
        AL[a-1].append(b-1)
        AL[b - 1].append(a - 1)
    vis = [-1] * n
    vis[s-1] = 0
    q = deque([(s-1,0)])
    #print(q, AL,edges)

    while q:
        u, d = q.popleft()
        for v in AL[u]:
            if vis[v] != -1: continue
            q.append((v,d+6))
            vis[v] = d +6

    vis = [i for i in vis if i != 0]

    return vis



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    q_itr = 0

    while q_itr < q:
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        q_itr += 1

        #fptr.write(' '.join(map(str, result)))
        #fptr.write('\n')

    #fptr.close()
