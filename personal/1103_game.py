import sys
sys.setrecursionlimit(2500)


def dfs(now):
    ret = 1
    if board[now[0]][now[1]] == 64:
        return 0
    for drc in directions:
        nxt = [now[0] + drc[0] * board[now[0]][now[1]], now[1] + drc[1] * board[now[0]][now[1]]]
        if 0 <= nxt[0] < N and 0 <= nxt[1] < M:
            if visited[nxt[0]][nxt[1]]:
                return -1

            if memoization[nxt[0]][nxt[1]]:
                ret = max(ret, memoization[nxt[0]][nxt[1]] + 1)
                continue

            visited[nxt[0]][nxt[1]] = 1
            ret_dfs = dfs(nxt)
            # -1, 즉 무한반복 가능 시 아예 기능을 종료해야 하는데, 재귀 시에는 반복해서 검사가 많이 수반된다. 따라서 반복이 좋아 보인다.
            if ret_dfs == -1:
                return -1

            ret = max(ret, ret_dfs + 1)
            visited[nxt[0]][nxt[1]] = 0

    memoization[now[0]][now[1]] = ret
    return ret


N, M = map(int, input().split())
board = [list(' '.join(input()).split()) for _ in range(N)]
for row in range(N):
    for col in range(M):
        if board[row][col] == 'H':
            board[row][col] = '64'

for row in range(N):
    board[row] = list(map(int, board[row]))

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
memoization = [[0] * M for _ in range(N)]

print(dfs([0, 0]))
