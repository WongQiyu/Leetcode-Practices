#curr * new
class Solution:
    def evalRPNSlow(self, tokens) -> int:
        symbols = {'+', '-', '*', '/'}
        stack = []
        for item in tokens:
            if item not in symbols:
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(eval(f'{a}{item}{b}')))
        return stack.pop()

class Solution:
    def evalRPN(self, tokens) -> int:
        sym = '+-*/'
        stack = []
        for d in tokens:
            if d not in sym:
                stack.append(int(d))
            else:
                a = stack.pop()
                if d == '+':
                    stack[-1 ] += a
                elif d == '-':
                    stack[-1] -= a
                elif d == '*':
                    stack[-1] *= a
                else:
                    stack[-1] = int(stack[-1] / a)
        return stack[0]


if __name__ == '__main__':
    print(Solution().evalRPN(["2","1","+","3","*"]))
    print(Solution().evalRPN(["4","13","5","/","+"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))