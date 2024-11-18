def numTeams(self, rating):
    c = 0
    for i, v in enumerate(rating):
        left_less, left_greater, right_less, right_greater = 0, 0, 0, 0
        for j in rating[:i]:
            if j < v:
                left_less += 1
            elif j > v:
                left_greater += 1
        for j in rating[i + 1:]:
            if j > v:
                right_greater += 1
            elif j < v:
                right_less += 1
        c += left_less * right_greater + left_greater * right_less
    return c

