from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #return Counter(ransomNote) <= Counter(magazine)
        a = Counter(ransomNote)
        b = Counter(magazine)
        for item in a:
            if a[item] > b.get(item,0):
                return False
        return True