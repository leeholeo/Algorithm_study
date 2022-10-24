# def making_colored_paper(n, lt=(0, 0)):
#     row = lt[0]
#     col = lt[1]
#     color_lt = paper[row][col]
#     for i in range(row, row+n):
#         for j in range(col, col+n):
#             if paper[i][j] != color_lt:
#                 nxt_n = n // 2
#                 w1, b1 = making_colored_paper(nxt_n, (row, col))
#                 w2, b2 = making_colored_paper(nxt_n, (row+nxt_n, col))
#                 w3, b3 = making_colored_paper(nxt_n, (row, col+nxt_n))
#                 w4, b4 = making_colored_paper(nxt_n, (row+nxt_n, col+nxt_n))
#                 break
#         else:
#             continue
#
#         break
#     else:
#         if color_lt:
#             return 0, 1
#         else:
#             return 1, 0
#
#     w = w1 + w2 + w3 + w4
#     b = b1 + b2 + b3 + b4
#     return w, b
#
#
# N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
#
# w, b = making_colored_paper(N)
# print(w)
# print(b)
def making_colored_paper(n, tl=(0, 0)):
    # 네 개의 어쩌구를 받음
    return 1
    return 0
    return -1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
squares = []
for i in range(1, 8):
    squares.append(1 << i)

q = []
for row in range(0, N, 2):
    for col in range(0, N, 2):
        q.append(((row, col), making_colored_paper(2, (row, col))))

top_left = [0, 0]
for n in squares:
    for top, left in q:
        making_colored_paper(n, (top, left))
        # 작은 사각형이 mono한지 검사
        # 최초에만 파랑 흰 갯수를 각각 세어 줘야 됨. 어캐하지?

    # 작은 사각형 합칠 수 있는지 검사

