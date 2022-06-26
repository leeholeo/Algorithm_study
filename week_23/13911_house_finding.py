# import heapq
# import sys
#
#
# def dijkstra(stores, store_limit):
#     near_stores = {}
#     for store in stores:
#         heap = []
#         for i in range(V):
#             if is_store[i]:
#                 continue
#             if edges[store][i] != -1 and edges[store][i] <= store_limit:
#                 near_stores[i] = min(near_stores[i], edges[store][i]) if near_stores.get(i) else edges[store][i]
#                 heapq.heappush(heap, (edges[store][i], i))
#         while heap:
#             weight, waypoint = heapq.heappop(heap)
#             if weight > edges[store][waypoint]:
#                 continue
#             for i in range(V):
#                 if is_store[i]:
#                     continue
#                 if edges[waypoint][i] == -1:
#                     continue
#                 next_weight = weight + edges[waypoint][i]
#                 if next_weight > store_limit:
#                     continue
#                 if edges[store][i] == -1 or next_weight < edges[waypoint][i]:
#                     near_stores[i] = min(near_stores[i], next_weight) if near_stores.get(i) else next_weight
#                     edges[store][i] = next_weight
#                     heapq.heappush(heap, (next_weight, i))
#     del heap
#     return near_stores
#
#
# def int_minus1(string):
#     return int(string) - 1
#
#
# input = sys.stdin.readline
# V, E = map(int, input().split())
# edges = [[-1] * V for _ in range(V)]
# for _ in range(E):
#     u, v, w = map(int_minus1, input().split())
#     w += 1
#     edges[u][v] = w if edges[u][v] == -1 else min(edges[u][v], w)
#     edges[v][u] = w if edges[v][u] == -1 else min(edges[v][u], w)
# _, mc_limit = map(int, input().split())
# mcdonalds = list(map(int_minus1, input().split()))
# _, star_limit = map(int, input().split())
# starbucks = list(map(int_minus1, input().split()))
# is_store = [False] * V
# for mc in mcdonalds:
#     is_store[mc] = True
# for star in starbucks:
#     is_store[star] = True
# mc_area = dijkstra(mcdonalds, mc_limit)
# star_area = dijkstra(starbucks, star_limit)
# min_dist = float('inf')
# for star_vertex, star_weight in star_area.items():
#     if mc_area.get(star_vertex):
#         min_dist = min(min_dist, star_weight + mc_area[star_vertex])
# print(min_dist)

'''
시간초과
'''

import heapq
import sys
from collections import defaultdict


def dijkstra1(stores, store_limit):
    for store in stores:
        heap = []
        for i in range(V):
            if edges[store].get(i, store_limit+1) <= store_limit:
                if is_store[i] is False:
                    near_stores[i] = edges[store][i]
                heapq.heappush(heap, (edges[store][i], i))
        while heap:
            weight, waypoint = heapq.heappop(heap)
            if weight > edges[store][waypoint]:
                continue
            for i, weight_next in edges[waypoint].items():
                next_weight = weight + weight_next
                if next_weight > store_limit:
                    continue
                if next_weight <= edges[store].get(i, store_limit):
                    if is_store[i] is False:
                        near_stores[i] = min(next_weight, near_stores.get(i, next_weight))
                    edges[store][i] = next_weight
                    heapq.heappush(heap, (next_weight, i))


def dijkstra2(stores, store_limit):
    min_dist = float('inf')
    for store in stores:
        heap = []
        for i in range(V):
            if edges[store].get(i, store_limit + 1) <= store_limit:
                if near_stores.get(i):
                    min_dist = min(min_dist, near_stores[i]+edges[store][i])
                heapq.heappush(heap, (edges[store][i], i))
        while heap:
            weight, waypoint = heapq.heappop(heap)
            if weight > edges[store][waypoint]:
                continue
            for i, weight_next in edges[waypoint].items():
                next_weight = weight + weight_next
                if next_weight > store_limit:
                    continue
                if next_weight <= edges[store].get(i, store_limit):
                    if near_stores.get(i):
                        min_dist = min(min_dist, near_stores[i] + edges[store][i])
                    edges[store][i] = next_weight
                    heapq.heappush(heap, (next_weight, i))
        return min_dist


def int_minus1(string):
    return int(string) - 1


input = sys.stdin.readline
V, E = map(int, input().split())
edges = defaultdict(dict)
for _ in range(E):
    u, v, w = map(int_minus1, input().split())
    w += 1
    # if u > v:
    #     u, v = v, u
    edges[u][v] = min(edges[u][v], w) if edges[u].get(v) else w
    edges[v][u] = min(edges[v][u], w) if edges[v].get(u) else w
_, mc_limit = map(int, input().split())
mcdonalds = list(map(int_minus1, input().split()))
_, star_limit = map(int, input().split())
starbucks = list(map(int_minus1, input().split()))
is_store = [False] * V
for mc in mcdonalds:
    is_store[mc] = True
for star in starbucks:
    is_store[star] = True
near_stores = {}
dijkstra1(mcdonalds, mc_limit)
min_distance = dijkstra2(starbucks, star_limit)
print(min_distance)
