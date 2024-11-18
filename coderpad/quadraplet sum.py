from collections import defaultdict


def find_quadruplet_sum_fast(numbers, target):
    # TODO: Code the same function as above, but faster!
    numbers = sorted(numbers)
    check = defaultdict(list)
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            suma = numbers[i] + numbers[j]
            if target - suma in check:
                a = check[target - suma]
                a.extend([numbers[i], numbers[j]])
                return a
            if suma not in check:
                check[suma] = [numbers[i], numbers[j]]


# =============== DO NOT EDIT BELOW THIS LINE ===============
import random
import sys
import time


def run_testcase(numbers, target, testcase_name):
    print(testcase_name.ljust(25), end='- ')
    sys.stdout.flush()
    t0 = time.time()
    result = find_quadruplet_sum_fast(numbers, target)

    elapsed = time.time() - t0

    if type(result) not in (tuple, list):
        print(f'FAILED: the function returned {result} of type {type(result)}, not a tuple or list.')
        sys.exit(1)

    if len(result) != 4:
        print(f'FAILED: the result has {len(result)} elements, not 4')
        sys.exit(1)

    if sum(result) != target:
        print(f'FAILED: the sum of {result} is {sum(result)}, not {target}')
        sys.exit(1)

    if any(r not in numbers for r in result):
        print('FAILED: one of the numbers is not in the list')
        sys.exit(1)

    print(f'PASSED')


run_testcase([5, 4, 3, 2, 1, 0], 11, 'Small testcase')
run_testcase([54, 3, 42, 16, 4, 24], 90, 'Solution with duplicates')
run_testcase([89, -62, -92, -37, 28, 29], -7, 'With negative numbers')
run_testcase([39, -57, -53, -79, 83, -6, 27, -97], 0, 'Target is zero')

for i in range(1, 6):
    numbers = random.sample(range(-100_000_000, 100_000_000), 1000)
    target = sum(numbers[-4:])  # Make sure the target can be done by summing the last 4 numbers
    random.shuffle(numbers)  # Shuffle the list to avoid cheaters who just return the last 4 elements ;)
    run_testcase(numbers, target, f'Large test #{i}')

print('Congratulations. You passed all testcases!')
