import sys


input = sys.stdin.readline
N, M = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(N)]
icebergs_indexs = []
cnt = 0
for row in range(N):
    for col in range(M):
        if icebergs[row][col]:
            cnt += 1
            icebergs_indexs.append((row, col))

time = 0
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
while cnt:
    time += 1
    temp_zeros = []
    i = 0
    while i < cnt:
        r, c = icebergs_indexs[i]
        drc_cnt = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if icebergs[nr][nc]:
                continue
            drc_cnt += 1

        if icebergs[r][c] <= drc_cnt:
            icebergs[r][c] = '0'
            cnt -= 1
            temp_zeros.append((r, c))
            icebergs_indexs.pop(i)
        else:
            icebergs[r][c] -= drc_cnt
            i += 1

    if cnt == 0:
        print(0)
        break

    for zr, zc in temp_zeros:
        icebergs[zr][zc] = 0

    stack = [icebergs_indexs[0]]
    block_cnt = 0
    visited = [[False] * M for _ in range(N)]
    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue

        visited[r][c] = True
        block_cnt += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if icebergs[nr][nc]:
                stack.append((nr, nc))

    if cnt != block_cnt:
        print(time)
        break

else:
    print(0)
