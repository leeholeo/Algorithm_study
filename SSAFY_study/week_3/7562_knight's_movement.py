from collections import deque


for tc in range(1, 1+int(input())):
    l = int(input())
    now = tuple(map(lambda x: int(x)+1, input().split()))
    destination = tuple(map(lambda x: int(x)+1, input().split()))
    if now == destination:
        print(0)
        continue

    directions = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))
    border = [[1] * (l+3)]
    board = [[1] + [0] * l + [1] * 2 for _ in range(l)]
    board = border + board + border * 2
    q = deque()
    q.append(now)
    while now != destination:
        now = q.popleft()
        for drc in directions:
            nxt = (now[0]+drc[0], now[1]+drc[1])
            if board[nxt[0]][nxt[1]]:
                continue

            board[nxt[0]][nxt[1]] = board[now[0]][now[1]] + 1
            q.append(nxt)

    print(board[now[0]][now[1]])
