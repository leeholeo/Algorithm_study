'''
다익스트라 기본
아직 구현에 속도와 정확도가 떨어진다. 연습하자.
'''
import heapq
import sys


def dijkstra():
    LIMIT = 987654321
    costs = [LIMIT] * (N+1)
    costs[1] = 0
    heap = [(0, 1)]
    while heap:
        accum_cost, stopover = heapq.heappop(heap)
        if accum_cost > costs[stopover]:
            continue
        for cost, destin in edges[stopover]:
            next_cost = accum_cost + cost
            if next_cost < costs[destin]:
                costs[destin] = next_cost
                heapq.heappush(heap, (next_cost, destin))
    return costs[N] if costs[N] != LIMIT else 'impossible'


input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
print(dijkstra())
