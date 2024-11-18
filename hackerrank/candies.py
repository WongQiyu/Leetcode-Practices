def candies(n, arr):
    res = [1] * n
    prev = arr[0]
    for i in range(1, n):
        if arr[i] > prev:
            res[i] = res[i-1] + 1
        prev = arr[i]
    for i in range(n-1, 0, -1):
        if arr[i - 1] > arr[i] and res[i] >= res[i-1]:
            res[i- 1] = res[i] + 1
    print(res)
    return sum(res)


# 1, 2, 1, 1
# 7, 9, 2 , 1

print(candies(3, [1,2,2]))
print(candies(10, [2,4,2,6,1,7,8,9,2,1]))
print(candies(8, [2,4,3,5,2,6,4,5,]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
