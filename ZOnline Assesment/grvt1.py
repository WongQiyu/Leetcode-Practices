# from collections import deque
# def solve (n):
#     score = 0
#     lst = deque(list(range(1, n + 1)))
#     tmp = deque([])
#     while len(lst) > 1:
#         pass
#     return score


def solve(n):
    targets = list(range(1, n + 1))
    score = 0

    while len(targets) > 1:
        # Remove every other target and add to score
        score += sum(targets[::2])
        targets = targets[1::2]

    # Add the last remaining target to the score


    return score


# Test the function
print(solve(5))  # Should return 11