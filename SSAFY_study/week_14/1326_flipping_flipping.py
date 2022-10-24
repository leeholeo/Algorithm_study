'''
BFS
'''
from collections import deque


N = int(input())
stones = list(map(int, input().split()))
start, end = map(lambda x: int(x)-1, input().split())
visited = [False] * N
visited[start] = 0
queue = deque()
queue.append(start)

# bfs
while queue:
    now = queue.popleft()
    # right jump
    nxt = now
    while nxt < N:
        if not visited[nxt]:
            visited[nxt] = visited[now] + 1
            queue.append(nxt)
        nxt += stones[now]
    # left jump
    nxt = now
    while nxt >= 0:
        if not visited[nxt]:
            visited[nxt] = visited[now] + 1
            queue.append(nxt)
        nxt -= stones[now]
    # destination check
    if visited[end]:
        print(visited[end]-1)
        break
else:
    print(-1)
