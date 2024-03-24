class Solution:
    def lengthOfLongestSubstringOld(self, s: str) -> int:
        l= 0
        char = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
    def lengthOfLongestSubstring(self, s: str):
        l,max_len = 0, 0
        seen = {}
        for r in range(len(s)):
            if s[r] not in seen:
                max_len = max(max_len, r-l+1)
            elif seen[s[r]] < l:
                max_len = max(max_len, r - l + 1)
            else:
                l = seen[s[r]] + 1
            seen[s[r]] = r
        return max_len
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))
