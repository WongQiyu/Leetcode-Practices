from collections import defaultdict
from heapq import nlargest
#https://algo.monster/liteproblems/1086
def high_five(items):
    score_dict = defaultdict(list)
    res = []
    for student_id, score in items:
        score_dict[student_id].append(score)
    for k,v in score_dict.items():
        average = sum(nlargest(5, v))//5
        res.append([k,average])
    return res

print(high_five([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))

# O(klogn)
#O(n) space
