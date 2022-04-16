from collections import deque


def island(row, col):
    q = deque()
    q.extend([(row, col)])
    while q:
        now_row, now_col = q.popleft()
        for drc in directions:
            nxt_row, nxt_col = now_row + drc[0], now_col + drc[1]
            if nxt_row < 0 or nxt_col < 0 or nxt_row >= h or nxt_col >= w:
                continue

            if field[nxt_row][nxt_col] == '1':
                field[nxt_row][nxt_col] = 0
                q.extend([(nxt_row, nxt_col)])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    field = [list(input().split()) for _ in range(h)]

    cnt = 0
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for i in range(h):
        for j in range(w):
            if field[i][j] == '1':
                island(i, j)
                cnt += 1

    print(cnt)
