'''
그냥 탐색
'''
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
campus = [input() for _ in range(N)]
DY = (-1, -1)
for row in range(N):
    for col in range(M):
        if campus[row][col] == 'I':
            DY = (row, col)

visited = [[False] * M for _ in range(N)]
stack = [DY]
cnt = 0
while stack:
    r, c = stack.pop()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc]:
            continue
        if campus[nr][nc] == 'X':
            continue
        visited[nr][nc] = True
        if campus[nr][nc] == 'P':
            cnt += 1
        stack.append((nr, nc))
print(cnt if cnt != 0 else "TT")
