import sys


def storm(top, left, size):
    half = size // 2
    bottom, right = top + size - 1, left + size - 1
    for i in range(half):
        for j in range(half):
            ices[top+j][right-i], ices[bottom-i][right-j], ices[bottom-j][left+i], ices[top+i][left+j] =\
                ices[top+i][left+j], ices[top+j][right-i], ices[bottom-i][right-j], ices[bottom-j][left+i]


def fire():
    memory = []

    for r in range(N):
        for c in range(N):
            if ices[r][c] == 0:
                continue

            cnt = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and ices[nr][nc]:
                    continue
                else:
                    cnt += 1

                if cnt == 2:
                    if ices[r][c] == 1:
                        memory.append((r, c))
                    else:
                        ices[r][c] -= 1

                    break

    for r, c in memory:
        ices[r][c] = 0


def count_block(row, col):
    stack = []
    ices[row][col] = 0
    stack.append((row, col))
    cnt = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and ices[nr][nc]:
                ices[nr][nc] = 0
                stack.append((nr, nc))
                cnt += 1

    return cnt


def find_biggest_block():
    counts = []
    for r in range(N):
        for c in range(N):
            if ices[r][c]:
                counts.append(count_block(r, c))

    return max(counts) if counts else 0


input = sys.stdin.readline
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, Q = map(int, input().split())
N = 2 ** N
ices = [list(map(int, input().split())) for _ in range(N)]
Ls = list(map(lambda x: 2 ** int(x), input().split()))
for L in Ls:
    for i in range(0, N, L):
        for j in range(0, N, L):
            storm(i, j, L)

    fire()

total_ice = 0
for ice in ices:
    total_ice += sum(ice)

print(total_ice)
print(find_biggest_block())
