'''
개인적으로 kruskal 선호, 따라서 prim 연습
:= walrus operator
'''
import sys
import heapq


V, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges[A].append((C, B))
    edges[B].append((C, A))
cnt = 1
visited = [False] * (V+1)
# 1에서 시작
visited[1] = True
heapq.heapify((heap := edges[1]))
total_weight = 0
while cnt < V:
    weight, vertex = heapq.heappop(heap)
    if visited[vertex]:
        continue
    visited[vertex] = True
    total_weight += weight
    cnt += 1
    for edge in edges[vertex]:
        heapq.heappush(heap, edge)
print(total_weight)
