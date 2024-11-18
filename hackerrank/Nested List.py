if __name__ == '__main__':
    checker = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        checker.append([name, score])

    second_low = sorted(list(set([x[1] for x in checker])))[1]
    res = [x[0] for x in checker if x[1] == second_low]
    res.sort()
    for item in res:
        print(item)