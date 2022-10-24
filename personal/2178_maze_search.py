from collections import deque


def maze_search(data):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque()
    s = [1, 1]
    q.append(s)
    data[s[0]][s[1]] = 0.1
    while True:
        try:
            now = q.popleft()
            for drc in direction:
                nxt = [now[0] + drc[0], now[1] + drc[1]]
                if data[nxt[0]][nxt[1]] == 1:
                    data[nxt[0]][nxt[1]] = data[now[0]][now[1]] + 1
                    if nxt == [N, M]:
                        return int(data[nxt[0]][nxt[1]]) + 1
                    q.append(nxt)

        except IndexError:
            return 0


N, M = map(int, input().split())
border = [[0] * (M + 2)]
data = [[0] + list(map(int, ' '.join(input()).split())) + [0] for _ in range(N)]
data = border + data + border

print(maze_search(data))
