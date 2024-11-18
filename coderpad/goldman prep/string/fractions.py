import math
import re
from fractions import Fraction
from functools import reduce


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator//denominator) + '.'
        numerator %= denominator
        i, part = 0, ''
        m = {numerator: i}
        while numerator % denominator:
            numerator *= 10
            i += 1
            rem = numerator % denominator
            part += str(numerator//denominator)
            if rem in m:
                part = part[:m[rem]] + '(' + part[m[rem]:] + ')'
                return res + part
            m[rem] = i
            numerator = rem

        return res + part

    def compress(self, chars):
        if len(chars) <= 1:
            return len(chars)
        rep = 0
        char = chars[0]
        res = 1
        for i in range(1,len(chars)):
            if chars[i] == char:
                if (rep % 10) == 0:
                    res += 1
                rep += 1
            else:
                res += 1
                rep = 0
                char = chars[i]
        return res

# print(Solution().fractionToDecimal(4,333))
# print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(Solution().compress(["a","a","b","b","c","c","c"]))