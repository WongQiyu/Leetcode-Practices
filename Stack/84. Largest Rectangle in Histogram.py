'''
Iterate through height.
Append (index, height) to new stack
But before we append, we check if previous height is greater than current height,
We do this by: stack[-1][1] > height.
since start = 0 is False we check this to see if stack is empty or has a value. (i.e. not empty)
if previous height is greater than current height, we append old_index instead. i.e. append(old_index, height)
We initial old_index = index and change it only when prev height > current height

After everything, we iterate through existing stack that did not 'have their indices changed or has been changed' to find the greatest area
'''
class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        for index, height in enumerate(heights):
            start = index
            while start and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h * (index - i) )
                start = i
            stack.append((start, height))
        for index, height in stack:
            max_area = max(max_area,height * (len(heights) - index))
        return max_area

    def largestRectangleAreaNeetcode(self, heights):
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, h_check = stack.pop()
                max_area = max(max_area,h_check * (i - index))
            stack.append((index, h))

        while stack:
            index, h_check = stack.pop()
            max_area = max(max_area,h_check * (len(heights) - index))
        return max_area


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
    print(Solution().largestRectangleArea([2, 4]))
    print(Solution().largestRectangleArea([1, 2,2]))
    #[1,2,3,4,5]