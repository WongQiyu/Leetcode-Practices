from collections import Counter
class Solution:
    def findAnagrams(self,s, p):
        actual_counter, counter = [0] * 128, [0] * 128
        for char in p:
            actual_counter[ord(char)] += 1
        for char in s[:len(p)]:
            counter[ord(char)] += 1
        res = []
        for i in range(0, len(s) - len(p)):
            if actual_counter == counter:
                res.append(i)
            counter[ord(s[i])] -= 1
            counter[ord(s[i + len(p)])] += 1
        if actual_counter == counter:
            res.append(len(s) - len(p))
        return res
    def findAnagramsOld(self, s: str, p: str):
        def compare(d1,d2):
            for k,v in d1.items():
                if d2.get(k,0) != v:
                    return False
            return True
        actual_counter = Counter(p)
        counter = Counter(s[:len(p)])
        res = []
        for i in range(0, len(s) - len(p)):
            if compare(actual_counter, counter):
                res.append(i)
            counter[s[i]] -= 1
            counter[s[i + len(p)]] += 1
        if compare(actual_counter, counter):
            res.append(len(s) - len(p))
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd","abc"))
    print(s.findAnagrams("abab", "ab"))