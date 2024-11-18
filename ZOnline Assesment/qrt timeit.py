#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import time
# from typing import Callable
#
#
# def delay_max(*args, **kwargs):
#     time.sleep(kwargs["delay"] / 1000)
#     return max(args)
#
#
# def delay_min(*args, **kwargs):
#     time.sleep(kwargs["delay"] / 1000)
#     return min(args)
#
#
# def delay_sum(*args, **kwargs):
#     time.sleep(kwargs["delay"] / 1000)
#     return sum(args)
#
#
# execution_time = []

#
# Complete the 'timeit' function below.
#
# The function is expected to return a function.
# The function accepts following parameter:
#  1. FUNCTION func
#
import time
import functools
import os

# Assuming execution_time is declared globally as a list
execution_time = []
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
          # Get the current time before executing the function
        start_time = time.time()
        result = func(*args, **kwargs)  # Execute the decorated function
        end_time = time.time()  # Get the current time after executing the function
        elapsed_time_ms = (end_time - start_time) * 1000  # Calculate elapsed time in milliseconds
        rounded = round(elapsed_time_ms)
        execution_time.append(rounded)
        print(execution_time)
        return result  # Return the result of the decorated function
    return wrapper

# Example usage of the decorator with a function
@timeit
def delay_max(*nums, delay):
    time.sleep(delay/1000)
    return max(nums)

@timeit
def delay_min(*nums, delay):
    time.sleep(delay/1000)
    return min(nums)

@timeit
def delay_sum(*nums, delay):
    time.sleep(delay/1000)
    return sum(nums)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    function_mapper = {
        "delay_max": delay_max,
        "delay_min": delay_min,
        "delay_sum": delay_sum,
    }

    for _ in range(n):
        row = input().rstrip().split()
        decorated_func = timeit(function_mapper[row[0]])
        args = row[1:-1]
        for i in range(len(args)):
            args[i] = int(args[i])
        print(str(decorated_func(*args, delay=int(row[-1]))) + "\n")

    error = 5

    for i in range(n):
        approx_execution_time = int(round(execution_time[i] / 50)) * 50
        if abs(execution_time[i] - approx_execution_time) > error:
            print("timeit didn't work as expected.\n")
            #fptr.write("timeit didn't work as expected.\n")
            #fptr.close()
            break
        else:
            execution_time[i] = approx_execution_time
    print(str(execution_time) + "\n")
    #fptr.write(str(execution_time) + "\n")

    #fptr.close()