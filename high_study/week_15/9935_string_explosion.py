'''
리스트 중간의 데이터를 지우거나 추가하는 경우에는 O(N)만큼의 시간이 소요되므로 주의해야 한다.
'''

# 1. KMP 응용, 시간초과
# 문제의 원인은 다른 곳에 있었으므로, KMP를 사용해서 다시 한 번 풀어보기
# import sys
#
#
# input = sys.stdin.readline
# string = input().strip()
# len_of_string = len(string)
# checked = [0] * len_of_string
# checked += [-1]
# explosion_string = input().rstrip()
# len_of_explosion = len(explosion_string)
# reversed_explosion_string = explosion_string[::-1]
#
# step_back = [0] * len_of_explosion
# start_idx = 1
# while start_idx < len_of_explosion - 1:
#     original_idx = 0
#     comparison = start_idx
#     while comparison < len_of_explosion:
#         if reversed_explosion_string[original_idx] == reversed_explosion_string[comparison]:
#             step_back[comparison] = original_idx
#             original_idx += 1
#             comparison += 1
#         else:
#             if start_idx == comparison:
#                 start_idx += 1
#             else:
#                 start_idx = comparison
#             break
#     else:
#         break
#
# # 중복 체크가 존재
# for idx in range(len_of_string-1, -1, -1):
#     last_number = checked[idx+1]
#     if string[idx] == reversed_explosion_string[last_number+1]:
#         checked[idx] = last_number + 1
#         if checked[idx] == len_of_explosion - 1:
#             checked[idx : idx+len_of_explosion] = []
#             string = string[:idx] + string[idx+len_of_explosion:]
#     else:
#         while step_back[last_number] or step_back[last_number+1]:
#             # last_number = step_back[last_number+1] - 1
#             now_number = step_back[last_number] + 1
#             if string[idx] == reversed_explosion_string[now_number]:
#                 checked[idx] = now_number
#                 break
#         else:
#             if string[idx] == reversed_explosion_string[0]:
#                 checked[idx] = 0
#             else:
#                 checked[idx] = -1
#
# if len(string) == 0:
#     print('FRULA')
# else:
#     print(string)


# 2. 단순 반복 체크 후 돌아오기, 시간초과
import sys
import time

str1 = 'A' * 100 ** 3
str2 = 'A' + 'B'*34 + 'A'

A_start_time = time.time()
input = sys.stdin.readline
string = list(' '.join(str1).split())
len_string = len(string)
explosion_string = str2.rstrip()
len_explosion = len(explosion_string)

idx = 0
cnt = 0
while idx < len_string:
    if string[idx] == explosion_string[cnt]:
        idx += 1
        cnt += 1
        if cnt == len_explosion:
            cnt = 0
            del string[idx-len_explosion : idx]
            idx -= 2*len_explosion - 1
            idx = max(idx, 0)
            len_string -= len_explosion
    else:
        if cnt:
            cnt = 0
        else:
            idx += 1

# if string:
#     print(*string, sep='')
# else:
#     print('FRULA')

A_end_time = time.time()
print(A_end_time - A_start_time)

# 3. 승열 코드
B_start_time = time.time()
# str1 = input()
str2 = str2[::-1]
stack = []
len_str1 = len(str1)
len_str2 = len(str2)

for i in range(len_str1-1, -1, -1):
    stack.append(str1[i])
    if stack[-1] == str2[-1] and ''.join(stack[-len_str2:]) == str2:
        del stack[-len_str2:]

ans_str = ''.join(reversed(stack))

# if ans_str == '':
#     print("FRULA")
# else:
#     print(ans_str)

B_end_time = time.time()
print(B_end_time - B_start_time)
