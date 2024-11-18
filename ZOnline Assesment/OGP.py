import math
def findmax(input1):
    curr_sum = total_sum = input1[0]
    loop_thru = input1[1:]
    for i in loop_thru:
        if i < curr_sum + i:
            curr_sum = i + curr_sum
        else:
            curr_sum = i
        total_sum = max(total_sum, curr_sum)

    return total_sum

from collections import Counter
def findpairs(input1,input2):
    from collections import Counter
    counter = dict(Counter(input1))
    checked = set()
    pairs = 0
    keys = list(counter.keys())

    def are_close(a, b, tol=1e-9):
        return abs(a - b) < tol

    for key in keys:
        other = input2 - key
    for key in keys:
        if key * 2 == input2:
            pairs += counter.get(key,0) //2
            continue
        other = input2 - key
        if other in keys:
            tup = (key,other) if key < other else (other,key)
            if tup not in checked:
                checked.add(tup)
                pairs += min(counter.get(key,0), counter.get(other,0))
    return pairs





if __name__ == '__main__':
    #print(findmax([1,6.25,-12,8.7]))
    #print(findmax([2.1, 3.62, -1.78, 2,-9,4.6]))
    print(findpairs([1.0,3.0,6.0,2.0,4.0,5.0,4.0,4.0, 2.0,2.0,6.0],8))
