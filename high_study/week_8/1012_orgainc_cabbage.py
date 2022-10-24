T = int(input())
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    cabbages = [[0] * N for __ in range(M)]
    for __ in range(K):
        r, c = map(int, input().split())
        cabbages[r][c] = 1

    for i in range(M):
        for j in range(N):
            if cabbages[i][j]:
                cnt += 1
                cabbages[i][j] = 0
                q = [(i, j)]
                while q:
                    r, c = q.pop()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (0 <= nr < M and 0 <= nc < N):
                            continue

                        if cabbages[nr][nc]:
                            cabbages[nr][nc] = 0
                            q.append((nr, nc))

    print(cnt)
