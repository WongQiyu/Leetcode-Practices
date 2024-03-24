class Solution:
    def longestPalindrome(self, s: str) -> int:
        memo = set()
        for token in s:
            memo.add(token) if token not in memo else memo.remove(token)

        odd = len(memo) > 0
        return len(s) - len(memo) + 1 if odd else len(s)