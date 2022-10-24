'''
완전탐색 back tracking
'''
def back_tracking(r, c, depth):
    if depth == K:
        if r == 0 and c == C-1:
            global cnt
            cnt += 1
        return

    visited[r][c] = True
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if field[nr][nc] == 'T':
            continue
        if visited[nr][nc]:
            continue
        back_tracking(nr, nc, depth+1)
    visited[r][c] = False


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
R, C, K = map(int, input().split())
field = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
cnt = 0
back_tracking(R-1, 0, 1)
print(cnt)
