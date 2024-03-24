class MyQueue:
    def __init__(self):
        # Enqueue stack
        self.in_stack = []
        # Dequeue stack
        self.out_stack = []

    def push(self, x):
        # Enqueue operation
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            # Transfer from enqueue stack to dequeue stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Dequeue operation
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            # Transfer from enqueue stack to dequeue stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Peek operation
        return self.out_stack[-1]

    def empty(self):
        # Check if both stacks are empty
        return not self.in_stack and not self.out_stack

""" 
class MyQueue:

    def __init__(self):
        # Initialize a deque to store the elements of the queue
        self.s = deque()

    def push(self, x: int) -> None:
        # Add an element to the back of the deque (enqueue operation)
        return self.s.append(x)

    def pop(self) -> int:
        # Remove and return the element from the front of the deque (dequeue operation)
        return self.s.popleft()

    def peek(self) -> int:
        # Return the element at the front of the deque without removing it
        return self.s[0]

    def empty(self) -> bool:
        # Check if the deque is empty
        if len(self.s) == 0:
            return True 
        else:
            return False 
"""