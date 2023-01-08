'''
2차원 누적합 + bfs
'''
from collections import deque
import sys


input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+1)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

if Sr == Fr and Sc == Fc:
    print(0)
    quit()

# 누적합
block = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            block.append((i, j))
            grid[i][j] = 0
for i, j in block:
    top = max(i-H+1, 0)
    left = max(j-W+1, 0)
    bottom = i+1
    right = j+1
    grid[top][left] -= 1
    grid[top][right] += 1
    grid[bottom][left] += 1
    grid[bottom][right] -= 1

now = 0
for i in range(N+1):
    for j in range(M+1):
        now += grid[i][j]
        grid[i][j] = now
now = 0
for j in range(M+1):
    for i in range(N+1):
        now += grid[i][j]
        grid[i][j] = now


# bfs
def bfs():
    queue = deque()
    queue.append((Sr, Sc))
    grid[Sr][Sc] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr <= N-H and 0 <= nc <= M-W):
                continue
            if grid[nr][nc] == 0:
                if nr == Fr and nc == Fc:
                    return grid[r][c]
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
    return -1


print(bfs())
