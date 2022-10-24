'''
stack, 역순으로 되돌리기
'''
string = input()
stack = []
for char in string:
    if char == 'P' and len(stack) >= 3 and stack[-1] == 'A' and stack[-2] == 'P' and stack[-3] == 'P':
        stack[-3:] = ['P']
    else:
        stack.append(char)
if stack == ['P']:
    print('PPAP')
else:
    print('NP')
