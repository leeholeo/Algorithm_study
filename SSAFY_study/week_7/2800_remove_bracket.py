def make_equations(bracket_idx):
    if bracket_idx == bracket_number:
        result.append(''.join(splited_equation))
        return
    # 괄호 포함
    splited_equation[left_bracket_idx[bracket_idx]] = '('
    splited_equation[right_bracket_idx[bracket_idx]] = ')'
    make_equations(bracket_idx+1)
    # 괄호 제거
    splited_equation[left_bracket_idx[bracket_idx]] = ''
    splited_equation[right_bracket_idx[bracket_idx]] = ''
    make_equations(bracket_idx+1)


equation = input()
splited_equation = []   # (와 ) 기준으로 문자열을 나눔, ex). ["123+12-", "(", "1153", ")", ..
left_bracket_idx = []   # (의 좌표가 splited_equation 기준으로 기록
right_bracket_idx = []
now = ''    # splited_equation에 들어가기 전에 문자열이 쌓이는 변수
bracket_idx = 0
bracket_stack = []  # 괄호 쌍을 유지하기 위해서 기록
for sign in equation:
    if sign == '(':
        bracket_stack.append(bracket_idx)
        bracket_idx += 1
        if now:
            splited_equation.append(now)
            now = ''
        left_bracket_idx.append(len(splited_equation))
        right_bracket_idx.append(None)
        splited_equation.append(sign)
    elif sign == ')':
        if now:
            splited_equation.append(now)
            now = ''
        right_bracket_idx[bracket_stack.pop()] = len(splited_equation)
        splited_equation.append(sign)
    else:
        now += sign
if now:
    splited_equation.append(now)

bracket_number = len(left_bracket_idx)
result = [] # 중복 제거용
make_equations(0)
result.sort()   # 정렬
before = result[0]
# 중복 제거
for res in result:
    if before != res:
        print(res)
    before = res
