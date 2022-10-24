'''
bfs
'''
from collections import deque
import sys


def bfs(edges, start):
    visited[start] = (cnt := 1)
    queue = deque()
    queue.append(start)
    while queue:
        u = queue.popleft()
        for v in edges[u]:
            if visited[v] == 0:
                cnt += 1
                visited[v] = cnt
                queue.append(v)


input = sys.stdin.readline()
N, M, R = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(1, N+1):
    edges[i].sort()
bfs(edges, R)
print(*visited[1:], sep='\n')
