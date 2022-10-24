import sys


class Queue:
    def __init__(self, size):
        self.q = [0] * size
        self.front = -1
        self.rear = -1

    def append(self, element):
        self.rear += 1
        self.q[self.rear] = element

    def pop(self):
        if self.front == self.rear:
            return None

        self.front += 1
        return self.q[self.front]


def ripe(cnt):
    if not cnt:
        return 0

    while True:
        coord = Q.pop()
        if coord is None:
            break

        height, row, col = coord
        for dh, dr, dc in directions:
            nh = height + dh
            nr = row + dr
            nc = col + dc
            if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M):
                continue

            if storages[nh][nr][nc]:
                continue

            Q.append((nh, nr, nc))
            storages[nh][nr][nc] = storages[height][row][col] + 1
            cnt -= 1

    if cnt:
        return -1

    return storages[height][row][col] - 1


input = sys.stdin.readline
M, N, H = map(int, input().split())
storages = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
directions = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
Q = Queue(100 ** 3 + 1)
count = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if storages[h][i][j] == 1:
                Q.append((h, i, j))
            elif storages[h][i][j] == 0:
                count += 1

print(ripe(count))
