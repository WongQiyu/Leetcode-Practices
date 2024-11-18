def solution (N, S):
    stack = []
    pointer = -1
    stack_count = -1
    #min pointer is -1
    for item in S:
        if item == 'back':
            if pointer == -1:
                pointer = 0
            pointer -= 1
        elif item == 'forward':
            pointer += 1
            if stack_count < pointer:
                pointer = stack_count
        else:
            if pointer < stack_count:
                stack = stack[:pointer+1]

            stack.append(item)
            pointer += 1
            stack_count = len(stack) - 1
    if len(stack) == 0:
        return '/home'
    return '/home/' + "/".join(stack)


# def solution(N,S):
#     history = ["/home"]
#     current = 0
#
#     for action in S:
#         if action == "back" and current > 0:
#             current -= 1
#         elif action == "forward" and current < len(history) - 1:
#             current += 1
#         elif action not in ["back", "forward"]:
#             current += 1
#             history = history[:current]
#             history.append(action)
#
#     return "/".join(history[:current + 1])


# Test case
#print(solution(["hackerearth", "contests", "back"]))
a= 'hackerearth contests back'
a  = list(map(str, a.split()))
print(solution(3,a))

a= 'forward forward forward forward forward'
a  = list(map(str, a.split()))
print(solution(5,a))

a= 'back forward ohamq iitqw forward back forward forward batjj forward'
a  = list(map(str, a.split()))
print(solution(10,a))

# Test cases
# print(solution(4,[ "food", "menu", "back", "forward"]))  # Output: home/food/menu
# print(solution(4,[ "food", "menu", "back", "diet"]))  # Output: home/food/diet
# print(solution(4,[ "food", "back", "menu", "forward"]))  # Output: home/menu