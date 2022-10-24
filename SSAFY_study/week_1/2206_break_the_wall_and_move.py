# import sys
#
#
# sys.setrecursionlimit(10 ** 4)
# input = sys.stdin.readline
# LARGE_NUMBER = 9876543210
# N, M = map(int, input().split())
# fields = [input() for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
# shortest = LARGE_NUMBER
#
#
# def dfs(r, c, hammer, cnt):
#     global shortest
#     if cnt > shortest:
#         return
#
#     if r == N - 1 and c == M - 1:
#         shortest = cnt
#         return
#
#     visited[r][c] = True
#     for dr, dc in directions:
#         nr = dr + r
#         nc = dc + c
#         if not (0 <= nr < N and 0 <= nc < M):
#             continue
#
#         if visited[nr][nc]:
#             continue
#
#         if fields[nr][nc] == '1':
#             if hammer:
#                 dfs(nr, nc, not hammer, cnt + 1)
#             else:
#                 continue
#         else:
#             dfs(nr, nc, hammer, cnt + 1)
#
#     visited[r][c] = False
#
#
# dfs(0, 0, True, 1)
# if shortest == LARGE_NUMBER:
#     print(-1)
# else:
#     print(shortest)

import sys


sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
LARGE_NUMBER = 987654
N, M = map(int, input().split())
fields = [input() for _ in range(N)]
dp = [[[0] * 2 for __ in range(M)] for _ in range(N)]
stack = [(0, 0, 0)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
cnt = 1
dp[0][0] = [1, 1]
while stack:
    cnt += 1
    temp_stack = []
    while stack:
        r, c, b = stack.pop()
        if r == N - 1 and c == M - 1:
            temp_stack = []
            break

        for dr, dc in directions:
            nr = dr + r
            nc = dc + c
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if dp[nr][nc][b]:
                continue

            if fields[nr][nc] == '1':
                if b == 1:
                    continue
                else:
                    dp[nr][nc][b + 1] = cnt
                    temp_stack.append((nr, nc, b + 1))
            else:
                if b == 0:
                    dp[nr][nc][b + 1] = cnt

                dp[nr][nc][b] = cnt
                temp_stack.append((nr, nc, b))

    stack = temp_stack


if dp[N - 1][M - 1][1]:
    result = dp[N - 1][M - 1][1]
    if dp[N - 1][M - 1][0]:
        result = min(result, dp[N - 1][M - 1][0])

    print(result)
else:
    print(-1)
