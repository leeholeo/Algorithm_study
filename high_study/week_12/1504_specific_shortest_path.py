import sys
import heapq


input = sys.stdin.readline
LARGE_NUM = 9876543210
N, E = map(int, input().split())
edges = [{} for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a][b] = min(edges[a].get(b, LARGE_NUM), c)
    edges[b][a] = min(edges[b].get(a, LARGE_NUM), c)

for i in range(N):
    edges[i][i] = 0

v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1
froms = [0, v1, v2]
for fromm in froms:
    hq = []
    for to, cost in edges[fromm].items():
        heapq.heappush(hq, (cost, to))

    while hq:
        now_cost, waypoint = heapq.heappop(hq)
        # if waypoint == N - 1:
        #     continue
        if now_cost > edges[fromm][waypoint]:
            continue

        for to, cost in edges[waypoint].items():
            new_cost = now_cost + cost
            if new_cost < edges[fromm].get(to, LARGE_NUM):
                edges[fromm][to] = new_cost
                edges[to][fromm] = new_cost
                heapq.heappush(hq, (new_cost, to))

path_a = edges[0].get(v1, LARGE_NUM) + edges[v1].get(v2, LARGE_NUM) + edges[v2].get(N - 1, LARGE_NUM)
path_b = edges[0].get(v2, LARGE_NUM) + edges[v2].get(v1, LARGE_NUM) + edges[v1].get(N - 1, LARGE_NUM)
# path_c = edges[0].get(v1, LARGE_NUM) + 2 * edges[v1].get(v2, LARGE_NUM) + edges[v1].get(N - 1, LARGE_NUM)
# path_d = edges[0].get(v2, LARGE_NUM) + 2 * edges[v2].get(v1, LARGE_NUM) + edges[v2].get(N - 1, LARGE_NUM)
# if path_a > LARGE_NUM:
#     print(-1)
# elif v1 == 0 and v2 == N - 1 and path_a == LARGE_NUM:
#     print(-1)
if path_a >= LARGE_NUM:
    print(-1)
else:
    print(min(path_a, path_b))
    # print(min(path_a, path_b, path_c, path_d))
