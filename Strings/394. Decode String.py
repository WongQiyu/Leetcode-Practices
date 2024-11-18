class Solution:
    def decodeString(self, s: str) -> str:
        stack, curr_num, curr_str = [], 0, ""
        for i in s:
            if i.isdigit():
                curr_num = curr_num * 10 + int(i)
            elif i.isalpha():
                curr_str += i
            elif i == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num, curr_str = 0, ""
            else:
                num = stack.pop()
                prev_string = stack.pop()
                curr_str = prev_string + curr_str * num
        return curr_str
# put old things in stack

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("2[abc]3[cd]ef"))
    print(s.decodeString("3[a2[c]]"))
