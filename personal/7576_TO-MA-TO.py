from collections import deque


def tomato(data, ripe, cnt):
    q = deque()
    q.extend(ripe)
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while True:
        try:
            now = q.popleft()
            for drc in direction:
                nxt = [now[0] + drc[0], now[1] + drc[1]]
                if data[nxt[0]][nxt[1]]:
                    continue
                cnt -= 1
                if cnt == 0:
                    return data[now[0]][now[1]]
                q.append(nxt)
                data[nxt[0]][nxt[1]] = data[now[0]][now[1]] + 1

        except IndexError:
            if cnt == 0:
                return 0
            return -1


M, N = map(int, input().split())
border = [[-1] * (M + 2)]
data = [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
data = border + data + border
ripe = []
cnt = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if data[i][j]:
            if data[i][j] == 1:
                ripe.append([i, j])
        else:
            cnt += 1

print(tomato(data, ripe, cnt))
