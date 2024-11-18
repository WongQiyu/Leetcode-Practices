from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        if not strs: return [""]
        d = defaultdict(list)
        for s in strs:
            tmp = ''.join(sorted(s))
            d[tmp].append(s)
        res = []
        for v in d.values():
            res.append(v)
        return res

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(""))
print(Solution().groupAnagrams("a"))