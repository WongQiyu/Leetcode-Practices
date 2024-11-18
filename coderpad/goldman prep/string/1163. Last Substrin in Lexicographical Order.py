class Solution:
    def lastSubstring(self, s: str) -> str:
        #i: starting index of first substring, #j starting index of second substring
        #k related tolength of substring
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            # first and second substring same, we keep increasing k
            if s[i+k] == s[j+k]:
                k += 1
                print(i,j,k,'a')
                continue
            elif s[i+k] > s[j+k]:
                #first substring is larger, j becomes j+k + 1 to compare
                j = j + k + 1
                print(i, j, k,'b')
            else:
                # first substring smaller, hence we increment starting index
                i = max(i + k + 1, j)
                j = i + 1
                print(i, j, k,'v')
            k = 0
        return s[i:]

print(Solution().lastSubstring("cacacb"))