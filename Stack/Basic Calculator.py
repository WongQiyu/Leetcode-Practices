class Solution:
    def calculate(self, s):
        num, sign, res = 0, 1 ,0
        stack = []
        s = s.strip()
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '-+':
                res += num * sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign *num
                res*= stack.pop()
                res += stack.pop()
                num = 0
        return res + num *sign

if __name__ == '__main__':
    s = Solution()
    print(s.calculate('(1+(4+5+2)-3)+(6+8)'))
    print(s.calculate('2-1+2'))
    print(s.calculate('1-11'))
    print(s.calculate("2147483647"))
    print(s.calculate('1-(     -2)'))

    #print(Solution().evalRPN(["2", "1", "+", "3", "*"]))