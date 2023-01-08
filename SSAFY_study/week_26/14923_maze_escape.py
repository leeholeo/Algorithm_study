'''
bfs
'''
from collections import deque


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x)-1, input().split())
Ex, Ey = map(lambda x: int(x)-1, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for __ in range(2)]
visited[1][Hx][Hy] = 1
visited[0][Hx][Hy] = 1
maze[Hx][Hy] = 1
queue = deque()
queue.append((Hx, Hy))
while queue:
    x, y = queue.popleft()
    for is_staff in range(2):
        if not visited[is_staff][x][y]:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if nx == Ex and ny == Ey:
                if min(visited[1][nx][ny], visited[0][nx][ny]) == 0:
                    print(max(visited[1][x][y], visited[0][x][y]))
                else:
                    print(min(visited[1][x][y], visited[0][x][y]))
                quit()
            if maze[nx][ny] == 0:
                if not visited[is_staff][nx][ny]:
                    visited[is_staff][nx][ny] = visited[is_staff][x][y] + 1
                    queue.append((nx, ny))
            else:
                if is_staff:
                    if not visited[is_staff-1][nx][ny]:
                        visited[is_staff-1][nx][ny] = visited[is_staff][x][y] + 1
                        queue.append((nx, ny))
else:
    print(-1)