from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hset = Counter(s)
        for i, c in enumerate(s):
            if hset[c] == 1:
                return i
        return -1
