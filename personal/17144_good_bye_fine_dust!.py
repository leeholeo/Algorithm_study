import sys


input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
R, C, T = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    if fields[i][0] == -1:
        upper_cleaner = i
        break

lower_cleaner = upper_cleaner + 1
for _ in range(T):
    temp_fields = [[0] * C for __ in range(R)]
    for r in range(R):
        for c in range(C):
            if c == 0 and (r == upper_cleaner or r == lower_cleaner):
                continue

            diffusion = fields[r][c] // 5
            cnt = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue

                if nc == 0 and (nr == upper_cleaner or nr == lower_cleaner):
                    continue

                cnt += 1
                temp_fields[nr][nc] += diffusion

            temp_fields[r][c] -= cnt * diffusion

    for r in range(R):
        for c in range(C):
            fields[r][c] += temp_fields[r][c]

    for r in range(upper_cleaner - 2, -1, -1):
        fields[r + 1][0] = fields[r][0]

    for r in range(lower_cleaner + 2, R):
        fields[r - 1][0] = fields[r][0]

    for c in range(1, C):
        fields[0][c - 1] = fields[0][c]

    for c in range(1, C):
        fields[-1][c - 1] = fields[-1][c]

    for r in range(1, lower_cleaner):
        fields[r - 1][-1] = fields[r][-1]

    for r in range(R - 2, upper_cleaner, -1):
        fields[r + 1][-1] = fields[r][-1]

    for c in range(C - 2, 0, -1):
        fields[upper_cleaner][c + 1] = fields[upper_cleaner][c]

    for c in range(C - 2, 0, -1):
        fields[lower_cleaner][c + 1] = fields[lower_cleaner][c]

    fields[upper_cleaner][1] = 0
    fields[lower_cleaner][1] = 0

result = 2
for r in range(R):
    result += sum(fields[r])

print(result)
