from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        kv = defaultdict
        for a in accounts:
            if a[0] not in kv:
                kv[a[0]] = [a[1:]]
                continue
            for kv
