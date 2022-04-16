# 폐기
# N = input().strip()
# int_N = int(N)
# length = len(N)
# M = int(input())
# if M == 0:
#     print(min(abs(int_N-100), length))
# elif M == 10:
#     print(abs(int_N - 100))
# else:
#     broken_buttons = list(map(int, input().split()))
#     buttons = [1] * 10
#     for b in broken_buttons:
#         buttons[b] = 0
#
#     for i in range(10):
#         if buttons[i]:
#             mini_btn = str(i)
#             break
#
#     for i in range(9, -1, -1):
#         if buttons[i]:
#             maxi_btn = str(i)
#             break
#
#     for idx in range(length):
#         if buttons[int(N[idx])]:
#             continue
#
#         def find_up(index):
#             if index < 0:
#                 if mini_btn == '0':
#                     if M == 9:
#                         return 987654321
#                     else:
#                         for i in range(1, 10):
#                             if buttons[i]:
#                                 second_mini_btn = str(i)
#                                 break
#
#                         return int(second_mini_btn * (length + 1))
#
#                 return int(mini_btn * (length + 1))
#             else:
#                 up = int(N[index]) + 1
#
#             while up < 10:
#                 if not buttons[up]:
#                     up += 1
#                     continue
#
#                 pre = N[:index] if index > 0 else ''
#                 return int(pre + str(up) + mini_btn * (length - (index + 1)))
#             else:
#                 return find_up(index - 1)
#
#         maxi = find_up(idx)
#
#         def find_down(index):
#             if index < 0:
#                 if length > 1:
#                     return int(maxi_btn * (length - 1))
#
#                 return -987654321
#             else:
#                 down = int(N[index]) - 1
#
#             while down >= 0:
#                 if not buttons[down]:
#                     down -= 1
#                     continue
#
#                 pre = N[:index] if index > 0 else ''
#                 return int(pre + str(down) + maxi_btn * (length - (index + 1)))
#             else:
#                 return find_down(index - 1)
#
#         mini = find_down(idx)
#
#         break
#     else:
#         maxi = int_N
#         mini = int_N
#
#     print(min(abs(maxi - int_N + len(str(maxi))), abs(int_N - mini + len(str(mini))), abs(int_N - 100)))
#     # print(maxi - int_N + len(str(maxi)))
#     # print(int_N - mini + len(str(mini)))
#     # print(abs(int_N - 100))
#     # print(maxi)
#     # print(mini)
#     # print(length)
N = input().strip()
int_N = int(N)
length = len(N)
M = int(input())
from_100 = abs(int_N - 100)
if M == 0:
    print(min(from_100, length))
elif M == 10:
    print(from_100)
else:
    broken_buttons = set(input().split())
    buttons = set(map(str, range(10)))
    buttons = buttons - broken_buttons
    combination = [[] for _ in range(7)]
    combination[0].append('')
    for i in range(6):
        temp_combination = []

        for c in combination[i]:
            for b in buttons:
                temp_combination.append(c + b)

        combination[i+1] = temp_combination

    mini = 9876543210
    for i in range(1, 7):
        for comb in combination[i]:
            int_comb = int(comb)
            comb = str(int_comb)
            len_comb = len(comb)
            mini = min(mini, abs(int_comb - int_N) + len_comb)

    mini = min(mini, from_100)
    print(mini)
