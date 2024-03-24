from collections import Counter, deque
class Solution:
    def minWindow(self,s, t):
        if len(t) > len(s): return ""
        map = [0] * 128
        l, r, l_index, min_len, count = 0, 0, 0, float('inf'), len(t)
        for k in t:
            map[ord(k)] += 1
        for r in range(len(s)):
            # only increase count if start in t
            if map[ord(s[r])] > 0:
                count -= 1
            map[ord(s[r])] -= 1
            while count == 0:
                if r - l  < min_len:
                    min_len = r - l
                    l_index = l
                if map[ord(s[l])] == 0:
                    count += 1
                map[ord(s[l])] += 1
                # increment start if first alphabet not needed
                l += 1
        return "" if min_len == float('inf') else  s[l_index:l_index+min_len + 1]
    def minWindowWrong(self, s: str, t: str) -> str:
        def all_in_counter(d):
            for k, v in counter.items():
                if d.get(k,0) < v:
                    return False
            return True

        if len(t) > len(s): return ""

        counter, check = Counter(t), {}
        store, t_len, flag = deque([]), len(t), False
        l_actual, r_actual, l_curr = -1, -1, -1

        for r in range(len(s)):
            if not counter[s[r]]:
                continue
            if l_curr == -1:
                l_curr = r
            check[s[r]] = check.get(s[r], 0) + 1
            store.append((r, s[r]))

            while r_actual != -1 and check[s[r]] > counter[s[r]]:
                _, val = store.popleft()
                check[val] -= 1
                flag = True
            if flag:
                l_curr = store[0][0]
                flag = False

            if len(store) >= t_len and all_in_counter(check):
                if r_actual == -1 or r - l_curr + 1 < r_actual - l_actual + 1:
                    l_actual, r_actual = l_curr, r

        return s[l_actual:r_actual+1]

#change 1: l_curr might not be 0 so its first index in counter
if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("bba", "ba"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("a", "a"))
    print(s.minWindow(  "ADOBECODEBANC", "ABC"))
    print(s.minWindow("ab", "b"))