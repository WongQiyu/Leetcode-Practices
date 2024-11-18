#!/bin/python3

import math
import os
import random
import re
import sys


class SumTable:
    def __init__(self, arr):
        self.arr = arr

    def get(self, i1, i2, j1, j2):
        total_sum = 0
        for row in self.arr[i1:i2]:
            total_sum += sum(row[j1:j2])
        return total_sum

    def set(self, i, j, k):
        self.arr[i][j] = k

    def __getitem__(self, key):
        if isinstance(key, list) and len(key) == 4:
            i, j = key
            return self.arr[i][j]
        else:
            raise IndexError("Invalid index for SumTable")

    def __setitem__(self, key, value):
        if isinstance(key, list) and len(key) == 2:
            i, j = key
            self.arr[i][j] = value
        else:
            raise IndexError("Invalid index for SumTable")

    # implement the remaining methods here


def performQueries(a, queries):
    table = SumTable(a)
    result = []

    for q_type, q_params in queries:
        if q_type == "get":
            i1, i2, j1, j2 = q_params
            res = table[i1:i2, j1:j2]
            result.append(res)
        elif q_type == "set":
            i, j, k = q_params
            table[i, j] = k
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    m = int(input())
    a = [[int(v) for v in input().split()] for _ in range(n)]

    queries = []
    q = int(input())
    for _ in range(q):
        q_tuple = input().split()
        q_type = q_tuple[0]
        q_params = [int(p) for p in q_tuple[1:]]
        queries.append((q_type, q_params))

    for res in performQueries(a, queries):
        print(('%d\n' % res))
        #fptr.write('%d\n' % res)

    #fptr.close()