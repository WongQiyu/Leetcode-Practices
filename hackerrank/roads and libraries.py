import math
import os
import random
import re
import sys
from math import inf
#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
def roadsAndLibraries(n, c_lib, c_road, cities):
    def dfs(u):
        vis[u] = True
        for v in AL[u]:
            if vis[v]: continue
            dfs(v)
    if c_road > c_lib:
        return c_lib * n
    AL = [[] for _ in range(n)]
    for u, v in cities:
        AL[u-1].append(v-1)
        AL[v-1].append(u-1)
    cc = 0
    vis = [False] * n
    for u in range(n):
        if not vis[u]:
            cc += 1
            dfs(u)
    return n * c_road + (c_lib - c_road) *cc



'''
STDIN       Function
-----       --------
2           q = 2
3 3 2 1     n = 3, cities[] size m = 3, c_lib = 2, c_road = 1
1 2         cities = [[1, 2], [3, 1], [2, 3]]
3 1
2 3
6 6 2 5     n = 6, cities[] size m = 6, c_lib = 2, c_road = 5
1 3         cities = [[1, 3], [3, 4],...]
3 4
2 4
1 2
2 3
5 6
'''
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
