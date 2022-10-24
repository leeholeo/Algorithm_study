import sys


def ladder_down(row, col, horizon_left):
    global maxi

    while row < H:
        while col < N - 1:
            if maxi >= horizon_left:
                break

            if horizons[row][col - 1] or horizons[row][col] or horizons[row][col + 1]:
                col += 1
                continue

            horizons[row][col] = True
            ladder_down(row, col + 2, horizon_left - 1)
            horizons[row][col] = False
            col += 1

        ladders[row + 1] = ladders[row][:]
        for idx in range(N - 1):
            if horizons[row][idx]:
                ladders[row + 1][idx], ladders[row + 1][idx + 1] = ladders[row][idx + 1], ladders[row][idx]

        col = 0
        row += 1

    if ladders[row] == ladders[0]:
        maxi = max(horizon_left, maxi)
        global flag
        flag = True


input = sys.stdin.readline
N, M, H = map(int, input().split())
horizons = [[False] * N for _ in range(H)]  # 가능성 판단에서 편하게 할라고 한 열 추가
for _ in range(M):
    a, b = map(int, input().split())
    horizons[a - 1][b - 1] = True

ladders = [[0] * N for _ in range(H + 1)]
ladders[0] = list(range(N))
maxi = 0
flag = False
ladder_down(0, 0, 3)

if flag:
    print(3 - maxi)
else:
    print(-1)
