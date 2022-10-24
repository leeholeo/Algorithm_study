# # 2차원 배열, 메모리 초과
# import heapq
#
#
# LARGE_NUM = -1
# V, E = map(int, input().split())
# K = int(input()) - 1
# pathes = [[LARGE_NUM] * V for _ in range(V)]
# heap = []
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     u -= 1
#     v -= 1
#     if pathes[u][v] == LARGE_NUM:
#         pathes[u][v] = w
#     else:
#         pathes[u][v] = min(pathes[u][v], w)
#
# for end in range(V):
#     weight = pathes[K][end]
#     if weight != LARGE_NUM:
#         heapq.heappush(heap, (weight, end))
#
# while heap:
#     weight, start = heapq.heappop(heap)
#     if pathes[K][start] < weight:
#         continue
#
#     for end in range(V):
#         if pathes[start][end] == LARGE_NUM:
#             continue
#
#         next_weight = weight + pathes[start][end]
#         if pathes[K][end] == LARGE_NUM or next_weight < pathes[K][end]:
#             pathes[K][end] = next_weight
#             heapq.heappush(heap, (next_weight, end))
#
# for end in range(V):
#     if pathes[K][end] == LARGE_NUM:
#         pathes[K][end] = 'INF'
#
# pathes[K][K] = 0
# for i in range(V):
#     print(pathes[K][i])


import sys
import heapq


input = sys.stdin.readline
LARGE_NUM = 9876543210
V, E = map(int, input().split())
K = int(input()) - 1
pathes = [{} for _ in range(V)]
heap = []
for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    pathes[u][v] = min(pathes[u].get(v, LARGE_NUM), w)

for end, weight in pathes[K].items():
    heapq.heappush(heap, (weight, end))

while heap:
    weight, start = heapq.heappop(heap)
    if pathes[K][start] < weight:
        continue

    for end in pathes[start].keys():
        next_weight = weight + pathes[start][end]
        if next_weight < pathes[K].get(end, LARGE_NUM):
            pathes[K][end] = next_weight
            heapq.heappush(heap, (next_weight, end))

shortest_pathes = ['INF'] * V
for end, weight in pathes[K].items():
    shortest_pathes[end] = weight

shortest_pathes[K] = 0
for i in range(V):
    print(shortest_pathes[i])
