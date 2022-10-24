'''
+: *2
-: 0
*: **2
/: 1
t -> s: 1로 가는 방법, s로 가는 방법
s -> t: 너무 고려할 게 많아서 포기
'''
# t -> s
def find_calcuation():
    if s == t:
        return 0
    stack = [(t, '')]
    found = []
    while stack:
        temp_stack = []
        while stack:
            number, calculation = stack.pop()
            if number == 1:
                found.append('/'+calculation)
            next_number = number // 2
            if number & 1 == 0:
                next_calculation = '+' + calculation
                if next_number == s:
                    found.append(next_calculation)
                temp_stack.append((next_number, next_calculation))
            sqrt = number ** 0.5
            next_number = int(sqrt)
            if sqrt % 1 == 0:
                next_calculation = '*' + calculation
                if next_number == s:
                    found.append(next_calculation)
                temp_stack.append((next_number, next_calculation))
        if found:
            found.sort()
            return found[0]
        stack = temp_stack
    return -1


s, t = map(int, input().split())
cnt = 0
print(find_calcuation())



# # s -> t
# s, t = map(int, input().split())
# cnt = 0
# cnt_s = 0
# cnt_2 = 0
# if t % s == 0:
#
# while t % s == 0:
#     cnt_s += 1
#     s **= 2
# cnt_s -= 1
# s **= 0.5
# s = int(s)
# t //= s
# while t % 2 == 0:
#     t //= 2
#     cnt_2 += 1
# if t > 1:
#     print(-1)
# else:
#     print(cnt_s + cnt_2 - 2**cnt_s + 1)
