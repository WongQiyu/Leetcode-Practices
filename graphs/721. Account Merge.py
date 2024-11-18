from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        storage = defaultdict()
        for account in accounts:
            if storage.get(account[0]):
                storage[account[0]] = storage[account[0]].append(account[1])


