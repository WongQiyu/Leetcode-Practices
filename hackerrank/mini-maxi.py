import math
import os
import random
import re
import sys
import math

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr = sorted(arr)
    mini = sum(arr[0:4])
    maxi = sum(arr[1:5])
    print(mini, maxi)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)