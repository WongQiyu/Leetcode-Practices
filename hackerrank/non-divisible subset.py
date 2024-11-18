def nonDivisibleSubset(k, s):
    from collections import Counter
    #c = Counter(s)
    #c_list = sorted(list(c.keys()))
    c_list = sorted(s)
    big_res = []
    checker = [[] for _ in range(len(c_list))]
    i = 0
    while i < len(c_list):
        if i-1 >= 0:
            if c_list[i-1] == c_list[i]:
                checker[i].append(checker[i-1])
                continue
        small_res = []
        for j in range(i, len(c_list)):
            if (c_list[j] + c_list[i]) % 4:
                small_res.append(c_list[j])