class Solution:
    def addBinary(self, a, b):
        i = 1
        j = 1
        carry = 0
        result = ''
        while i <= len(a) or j <= len(b) or carry > 0:
            if i <= len(a):
                carry += int(a[-i])
                i+= 1
            if j <= len(b):
                carry += int(b[-j])
                j+= 1
            result = str(carry % 2) + result
            carry //= 2
        return result
if __name__ == '__main__':
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))