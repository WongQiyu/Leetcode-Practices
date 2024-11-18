#(3, 10, 14, 20, 1, 5)
# (1, 10, 14, 20)

'''
unpaint_instructions = analyze_paint_logs((3, 10, 14, 20, 1, 5))
    print(unpaint_instructions)
    assert unpaint_instructions == [1, 1, 10, 1, 14, 20]

    unpaint_instructions = analyze_paint_logs((1, 7, 1, 7, 1, 11, 1, 7, 1, 7))
    print(unpaint_instructions)
    assert unpaint_instructions == [5, 1, 7, 1, 7, 11]
'''
def analyze_paint_logs(coords):
    cord = [[coords[i], coords[i+1]] for i in range (0, len(coords), 2)]
    cord.sort(key=lambda x: (x[0],x[1]))
    print(cord)
    curr_count = 0
    curr = cord[0]
    res = []
    for val in cord:
        s, e = val[0], val[1]
        ns, ne = curr[0], curr[1]
        if ne < s:
            res.extend([1,ns, ne]) if curr_count < 5 else res.extend([5,ns, ne])
            curr = [s,e]
            curr_count = 0
        elif ne >= s and curr_count < 5:
            curr = [ns,max(e,ne)]
            curr_count += 1
        else:
            curr = [ne,max(e,ne)]
    res.extend([1, curr[0], curr[1]]) if curr_count < 5 else res.extend([5, curr[0], curr[1]])
    return res


def merge(intervals):
    res = []
    intervals.sort(key=lambda x: (x[0],x[1]))
    curr = intervals[0]
    print(intervals)
    for val in intervals:
        s, e = val[0], val[1]
        ns, ne = curr[0], curr[1]
        if ne < s:
            res.append(curr)
            curr = [s,e]
        else:
            curr = [ns,max(e,ne)]
    res.append(curr)
    return res

def main():
    unpaint_instructions = analyze_paint_logs((3, 10, 14, 20, 1, 5))
    print(unpaint_instructions)
    assert unpaint_instructions == [1, 1, 10, 1, 14, 20]

    unpaint_instructions = analyze_paint_logs((1, 7, 1, 7, 1, 11, 1, 7, 1, 7))
    print(unpaint_instructions)
    assert unpaint_instructions == [5, 1, 7, 1, 7, 11]

    unpaint_instructions = analyze_paint_logs(
        (
            5.2, 10.7, 5.3, 10.6, 5.0, 10.9, 5.1, 10.8,
            7.7, 8.8, 6.6, 7.7, 7.0, 8.0,
            1.5, 2.3, 1.6, 2.1, 2.3, 3.4,
        )
    )
    print(unpaint_instructions)
    assert unpaint_instructions == [
        1, 1.5, 3.4,
        1, 5.0, 6.6,
        5, 6.6, 8.8,
        1, 8.8, 10.9
    ]


if __name__ == "__main__":
    #print(analyze_paint_logs((3, 10, 14, 20, 1, 5)))
    print(analyze_paint_logs((1, 7, 1, 7, 1, 11, 1, 7, 1, 7)))
    #main()