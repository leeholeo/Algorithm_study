import sys


input = sys.stdin.readline
N, M, K = map(int, input().split())
# r, c, m, s, d
fireballs = [[[] for _ in range(N)] for _ in range(N)]
directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
directions = directions[::-1]
for _ in range(M):
    r, c, *fireball = map(int, input().split())
    fireballs[r-1][c-1].append(fireball)

for _ in range(K):
    temp_fireballs = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for m, s, d in fireballs[r][c]:
                nr = (r + directions[d][0] * s) % N
                nc = (c + directions[d][1] * s) % N
                temp_fireballs[nr][nc].append((m, s, d))

    for r in range(N):
        for c in range(N):
            if len(temp_fireballs[r][c]) <= 1:
                continue

            tm, ts, td = 0, 0, 0
            cnt = 0
            for m, s, d in temp_fireballs[r][c]:
                tm += m
                ts += s
                d %= 2
                cnt += 1
                td += d

            rm = tm // 5
            if rm == 0:
                temp_fireballs[r][c] = []
                continue

            rs = ts // cnt
            if td == 0 or td == cnt:
                rd = 0
            else:
                rd = 1

            temp_fireballs[r][c] = [(rm, rs, rd), (rm, rs, rd+2), (rm, rs, rd+4), (rm, rs, rd+6)]

    fireballs = temp_fireballs

total_mass = 0
for r in range(N):
    for c in range(N):
        for m, _, __ in fireballs[r][c]:
            total_mass += m

print(total_mass)
