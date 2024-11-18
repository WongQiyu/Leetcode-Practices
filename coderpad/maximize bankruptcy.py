import math

def get_biggest_loss(prices):
    max_val = 0
    min_diff = 0
    for item in prices:
        diff = item - max_val
        if diff < min_diff:
            min_diff = diff
        if item > max_val:
            max_val = item
    return min_diff

loss = get_biggest_loss((3, 2, 4, 2, 1, 5))
assert loss == -3
print(loss)

# Maximum Loss between the first and last values
loss = get_biggest_loss((5, 3, 4, 2, 3, 1))

assert loss == -4
print(loss)
# Profit with a flat part
loss = get_biggest_loss((1, 2, 4, 4, 5))
assert loss == 0
print(loss)
# Constant Profit
loss = get_biggest_loss((3, 4, 7, 9, 10))
assert loss == 0
print(loss)
# All flat
loss = get_biggest_loss((42, 42, 42, 42, 42))
assert loss == 0
print(loss)
# One element
loss = get_biggest_loss((1000, ))
assert loss == 0
print(loss)
# Varied
loss = get_biggest_loss((30, 20, 100, 70, 150, 140))
assert loss == -30
print(loss)