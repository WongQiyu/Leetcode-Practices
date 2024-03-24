class Solution:
    def myAtoi(self, s: str) -> int:
        digi = set('0123456789')
        MAX, MIN = 2147483647, -2147483648
        s = s.strip()
        res, sign = 0, 1
        i = 1 if s and s[0] in '+-' else 0
        sign = - 1 if i == 1 and s[0] == '-' else 1
        while i < len(s) and s[i] in digi:
            res = (res * 10) + int(s[i])
            i += 1
        res *= sign
        return max(MIN, min(MAX, res))


