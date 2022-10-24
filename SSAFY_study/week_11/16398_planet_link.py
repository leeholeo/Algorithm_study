'''
MST
Kruskal
'''
import heapq


def find(node):
    if parents[node] == -1:
        return node
    else:
        pn = find(parents[node])
        parents[node] = pn
        return pn


def union(node2):
    p2 = find(node2)
    if START != p2:
        parents[p2] = START
        return True
    else:
        return False


START = 0
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
parents = [-1] * N
heap = []
for j in range(1, N):
    heapq.heappush(heap, (costs[START][j], j))

cnt = 1
total_cost = 0
while cnt < N:
    cost, target = heapq.heappop(heap)
    if union(target):
        cnt += 1
        total_cost += cost
        for j in range(N):
            if find(j) == START:
                continue
            heapq.heappush(heap, (costs[target][j], j))
print(total_cost)
