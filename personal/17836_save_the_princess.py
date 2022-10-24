from collections import deque


def maze_search(data, t):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque()
    s = [1, 1]
    q.append(s)
    data[s[0]][s[1]] = 0.1
    t_sword = 1234567890
    while True:
        try:
            now = q.popleft()
            cnt = data[now[0]][now[1]]
            if int(cnt) == min(t, t_sword):
                raise IndexError
            for drc in direction:
                nxt = [now[0] + drc[0], now[1] + drc[1]]

                if data[nxt[0]][nxt[1]] == 0:
                    data[nxt[0]][nxt[1]] = cnt + 1
                    if nxt == [N, M]:
                        return int(data[nxt[0]][nxt[1]])
                    q.append(nxt)

                elif data[nxt[0]][nxt[1]] == 2:
                    data[nxt[0]][nxt[1]] = cnt + 1
                    sword = int(data[nxt[0]][nxt[1]] + (N - nxt[0] + M - nxt[1]))
                    if sword <= t:
                        t_sword = sword
                    continue

        except IndexError:
            if t_sword == 1234567890:
                return 'Fail'
            else:
                return t_sword


N, M, T = map(int, input().split())
border = [[1] * (M + 2)]
data = [[1] + list(map(int, ' '.join(input()).split())) + [1] for _ in range(N)]
data = border + data + border

print(maze_search(data, T))
