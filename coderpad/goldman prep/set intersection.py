from collections import Counter

def inters_elem(arr1,arr2):
    res = Counter(arr1) & Counter(arr2)
    final = []
    for k,v in res.items():
        final.extend([k] *v)
    return final
print(inters_elem([1,1,2,2,2], [1,1,1,2,2,3,4,5]))