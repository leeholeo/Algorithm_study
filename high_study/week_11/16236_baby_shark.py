from collections import deque


def bfs():
    global shark_idx, shark_size, shark_eat
    q = deque()
    q.append(shark_idx)
    cnt = 0
    will_eat = (N, N)
    visited = [[False] * N for _ in range(N)]
    while q:
        cnt += 1
        temp_q = deque()
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = True
                if fishes[nr][nc] > shark_size:
                    continue
                elif fishes[nr][nc] == 0 or fishes[nr][nc] == shark_size:
                    temp_q.append((nr, nc))
                else:
                    will_eat = min(will_eat, (nr, nc))

        if will_eat != (N, N):
            fishes[will_eat[0]][will_eat[1]] = 0
            shark_idx = will_eat
            shark_eat += 1
            if shark_size == shark_eat:
                shark_size += 1
                shark_eat = 0

            return cnt

        q = temp_q

    return 0


N = int(input())
fishes = [list(map(int, input().split())) for _ in range(N)]
shark_idx = ()
shark_size = 2
shark_eat = 0
time = 0
directions = ((-1, 0), (0, -1), (0, 1), (1, 0)) # 상좌우하
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            fishes[i][j] = 0
            shark_idx = (i, j)

dt = 1
while dt:
    dt = bfs()
    time += dt

print(time)
