from collections import deque


def maze_making():
    q = deque()
    nxt_q = []
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    now = [0, 0]
    cnt = 0
    q.append(now)

    while True:
        now = q.popleft()
        for d in direction:
            nxt = [now[0] + d[0], now[1] + d[1]]

            if nxt[0] < 0 or nxt[0] >= N or nxt[1] < 0 or nxt[1] >= N:
                continue
            elif nxt == [N - 1, N - 1]:
                return cnt
            elif visited[nxt[0]][nxt[1]]:
                continue

            if data[nxt[0]][nxt[1]]:
                q.append(nxt)
            else:
                nxt_q.append(nxt)
            visited[nxt[0]][nxt[1]] = 1

        if not q:
            for ele in nxt_q:
                q.append(ele)
            nxt_q.clear()
            cnt += 1


N = int(input())
data = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

print(maze_making())

# 1. 연결되어 있는 1을 모조리 queue에 추가한다(외각만)
# 2. 끝 점이 포함되어 있으면 종료한다.
# 3. 벽이면 next_queue에 넣는다.
# 4. queue가 종료되면 next_queue를 실행한다.
# 5. 1 ~ 3을 반복한다.
