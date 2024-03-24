
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
            return
        if val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self) -> None:
        check = self.stack.pop()
        self.min_stack.pop()
        return check

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.pop()
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.getMin()
    print(param_4)