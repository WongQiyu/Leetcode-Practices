from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        store = deque()
        closed = {']', '}',')'}
        d = {'[':']', '{':'}','(':')'}
        while s:
            tmp = s.pop()
            if tmp in closed:
                store.append(tmp)
            elif store:
                b = store.pop()
                if d[tmp] != b:
                    return False
            else:
                return False
        if store:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))

