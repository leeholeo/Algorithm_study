'''
괄호 처리? 바로 stack
'''
WEIGHT = {
    'H': 1,
    'C': 12,
    'O': 16
}
formula = input()
num_stack = []
bracket_stack = []
for i in range(len(formula)):
    char = formula[i]
    if char == '(':
        bracket_stack.append(len(num_stack))
    elif char == ')':
        if len(num_stack) != bracket_stack[-1]:
            bracket_start = bracket_stack.pop()
            num_stack[bracket_start:] = [sum(num_stack[bracket_start:])]
        else:
            bracket_stack.pop()
    elif char in WEIGHT:
        num_stack.append(WEIGHT[char])
    else:
        num_stack[-1] *= int(char)
print(sum(num_stack))
