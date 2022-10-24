def swap(order, lad):
    new_order = ''
    i = 0
    while i < k - 1:
        if lad[i] == '*':
            new_order += order[i]
            i += 1
        elif lad[i] == '-':
            new_order += order[i+1] + order[i]
            i += 2

    if i == k - 1:
        new_order += order[-1]

    return new_order


k = int(input())
n = int(input())
end_order = input()
ladders = [input() for _ in range(n)]
unknown = 0
for idx, ladder in enumerate(ladders):
    if ladder[0] == '?':
        unknown = idx
        break

start_order = ''.join(map(lambda x: chr(ord('A') + x), range(k)))
for idx in range(unknown):
    start_order = swap(start_order, ladders[idx])

for idx in range(n - 1, unknown, -1):
    end_order = swap(end_order, ladders[idx])

unknown_ladder = ''
start_order += 'a'
end_order += 'a'
start_order = list(start_order)
end_order = list(end_order)
idx = 0
for idx in range(k - 1):
    if start_order[idx] == end_order[idx]:
        unknown_ladder += '*'
    elif start_order[idx] == end_order[idx + 1] and start_order[idx + 1] == end_order[idx]:
        unknown_ladder += '-'
        start_order[idx], start_order[idx + 1] = start_order[idx + 1], start_order[idx]
    else:
        print('x' * (k - 1))
        break
else:
    print(unknown_ladder)



# # 정용우
#
# def ladder(board, first, togo):  #보드, 초기조건, 목적지
#     middle = ['@'] * (k)
#     for start in range(k):
#         i, j = 0, start
#         # print('start', start, first[start])
#         while True:
#             # print(i, j)
#             if i == togo:
#                 middle[j] = first[start]
#                 break
#             if 1 <= j < k and board[i][j-1] == '-':  # 왼쪽
#                 i, j = i+1, j-1
#             elif 0 <= j < k-1 and board[i][j] == '-':  # 오른쪽
#                 i, j = i+1, j+1
#             else:
#                 i, j = i+1, j
#     return middle
#
#
# dir = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 우좌하상
# k = int(input())  # 사람의 수
# n = int(input())  # 가로 줄 길이
# first = ''
# for i in range(65, 65+k):
#     first += chr(i)
# final = input()  # 최종 순서
# board = [list(input()) for _ in range(n)]
# hidden = 0
# for row, b in enumerate(board):
#     if b.count('?'):
#         hidden = row
#
# # * 이면 오른쪽이랑 연결되어있다는 것.
# top = ladder(board, first, hidden)
# bot = ladder(board[::-1], final, n - 1 - hidden)
# # print(*first)
# # print('--------------')
# # print(*bot)
# # print(*top)
# # print('-------------')
# # print(*final)
#
# # '??'인 부분의 초기상태를 *로 해준 후
# # 자리를 바꾸어 같은 값이면 '*'을 '-'로 바꾸어준다.
# ans = ['*' for _ in range(k-1)]
# swapped = False
# for i in range(k-1):
#     if bot[i] == top[i+1] and bot[i+1] == top[i]:
#         ans[i] = '-'
#         bot[i], bot[i+1] = bot[i+1], bot[i]
#         swapped = True
#     if swapped:
#         swapped = False
# # 바꾼 start와 final이 같으면 성공!
# # 아니면 x를 출력한다.
# if bot != top:
#     ans = ['x' for _ in range(k-1)]
# print(''.join(ans))
#
# # answer = ['*'] * (k-1)
# # for i in range(k):
# #     if bot[i] == top[i]:
# #         continue
# #     elif i >= 1 and bot[i] == top[i-1]:# and answer[i]:
# #         answer[i-1] = '-'
# #     elif i+1 < k and bot[i] == top[i+1]:
# #         continue
# #     else:
# #         answer = ['x'] * (k-1)
# #
# # for i in range(k-1):
# #     if answer[i] == '-' and answer[i+1] == '-':
# #         answer = ['x'] * (k-1)
# # print(''.join(answer))
#
