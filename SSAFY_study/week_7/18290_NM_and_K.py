'''
완전탐색
'''
import sys


def recursion(row_col, k, summation):
    if row_col == N * M:
        return

    row, col = divmod(row_col, M)
    # 사방탐색
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc]:
            break
    # for문에서 break가 터지지 않았을 시 else 문, for ~ else ~
    else:
        if k == 1:
            global result
            result = max(result, summation + grid[row][col])
        else:
            # backtracking
            visited[row][col] = True
            recursion(row_col+1, k-1, summation + grid[row][col])
            visited[row][col] = False
    recursion(row_col+1, k, summation)


MIN = -987654321
input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = MIN
recursion(0, K, 0)
print(result)
