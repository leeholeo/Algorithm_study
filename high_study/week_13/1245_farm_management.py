M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(M)]
directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
cnt = 0
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue

        flag = True
        visited[i][j] = 1
        peaks = [(i, j)]
        while peaks:
            r, c = peaks.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not(0 <= nr < M and 0 <= nc < N):
                    continue

                if farm[r][c] > farm[nr][nc]:
                    continue
                elif farm[r][c] == farm[nr][nc]:
                    if visited[nr][nc]:
                        continue

                    visited[nr][nc] = 1
                    peaks.append((nr, nc))
                else:
                    flag = False

        if flag:
            cnt += 1

print(cnt)
