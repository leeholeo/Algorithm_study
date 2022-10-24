"""
위, 아래, 전, 후, 좌, 우 6방향으로 봤을 때로 나눠서 더하기
위, 아래는 고정
전, 후, 좌, 우는 각 점에서 사방탐색을 할 경우 인접 점이 해당 점보다 작은 경우 그 차만큼 겉넓이가 나옴
"""
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


N, M = map(int, input().split())
cubes = [list(map(int, input().split())) for _ in range(N)]
surface = 2 * N * M
for r in range(N):
    for c in range(M):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                surface += cubes[r][c]
                continue
            surface += max(0, cubes[nr][nc]-cubes[r][c])

print(surface)
