def triplets(t, d):
    d.sort()  # Sort the list in ascending order
    n = len(d)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = d[i] + d[left] + d[right]

            if current_sum <= t:
                # All triplets between left and right are valid
                count += right - left
                left += 1
            else:
                right -= 1

    return count

print(triplets([1,2,3,4,6],8))