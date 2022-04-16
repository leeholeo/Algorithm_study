import sys


def tornado(iteration):
    global r, c, d
    # front, side1, side2, rear
    (fr, fc), (sr, sc) = directions[d], directions[d+1]
    for _ in range(iteration):
        nr, nc = r + fr, c + fc
        s = sands[nr][nc]
        s1, s2, s5, s7, s10 = s // 100, s // 50, s // 20, (s * 7) // 100, s // 10
        s_remainder = s - 2 * (s1 + s2 + s7 + s10) - s5

        sands[nr][nc] = 0
        if 0 <= r + 3 * fr < N and 0 <= c + 3 * fc < N:
            sands[r + 3 * fr][c + 3 * fc] += s5
        for sign in (1, -1):
            if 0 <= r + sign * sr < N and 0 <= c + sign * sc < N:
                sands[r + sign * sr][c + sign * sc] += s1
            if 0 <= nr + sign * 2 * sr < N and 0 <= nc + sign * 2 * sc < N:
                sands[nr + sign * 2 * sr][nc + sign * 2 * sc] += s2
            if 0 <= nr + sign * sr < N and 0 <= nc + sign * sc < N:
                sands[nr + sign * sr][nc + sign * sc] += s7
            if 0 <= nr + fr + sign * sr < N and 0 <= nc + fc + sign * sc < N:
                sands[nr + fr + sign * sr][nc + fc + sign * sc] += s10

        if 0 <= nr + fr < N and 0 <= nc + fc < N:
            sands[nr + fr][nc + fc] += s_remainder

        r, c = nr, nc

    d = (d + 1) % 4


input = sys.stdin.readline
N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]
total = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] + [(0, -1)]
for sand in sands:
    total += sum(sand)

r, c = N // 2, N // 2
d = 0
for i in range(1, N):
    tornado(i)
    tornado(i)

tornado(N - 1)

end_total = 0
for sand in sands:
    end_total += sum(sand)

print(total - end_total)
