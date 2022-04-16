def heap_push(heap, value):
    heap.append(value)
    now = len(heap) - 1
    while now:
        pv = now // 2 - (now % 2 ^ 1)
        if heap[pv] > heap[now]:
            heap[pv], heap[now] = heap[now], heap[pv]
            now = pv
        else:
            break


def heap_pop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    rtn = heap.pop(-1)
    temp = 0
    while temp != -1:
        now = temp
        temp = -1
        cv1 = now * 2 + 1
        cv2 = now * 2 + 2
        try:
            if heap[now] > heap[cv1]:
                heap[now], heap[cv1] = heap[cv1], heap[now]
                temp = cv1
            if heap[now] > heap[cv2]:
                heap[now], heap[cv2] = heap[cv2], heap[now]
                temp = cv2
        except IndexError:
            break
    return rtn


import sys


input = sys.stdin.readline
# ver 2
n = int(input())
m = int(input())
costs = [[0] * n for _ in range(n)]
h = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if costs[a][b]:
        if costs[a][b] <= c:
            continue

    costs[a][b] = c
    heap_push(h, (c, a, b))

while h:
    cost, now, to = heap_pop(h)
    for j in range(n):
        if j == now or costs[to][j] == 0:
            continue

        next_cost = costs[to][j] + cost
        if costs[now][j] == 0 or costs[now][j] > next_cost:
            costs[now][j] = next_cost
            heap_push(h, (next_cost, now, j))

for cost in costs:
    print(*cost)


# # ver 1
# n = int(input())
# m = int(input())
# costs = [[0] * n for _ in range(n)]
# h = []
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     if costs[a][b]:
#         if costs[a][b] <= c:
#             continue
#
#     costs[a][b] = c
#     heap_push(h, (c, a, b))
#
# while h:
#     cost, now, to = heap_pop(h)
#     for i in range(n):
#         if i == to or costs[i][now] == 0:
#             continue
#
#         next_cost = costs[i][now] + cost
#         if costs[i][to] == 0 or costs[i][to] > next_cost:
#             costs[i][to] = next_cost
#             heap_push(h, (next_cost, i, to))
#
# for cost in costs:
#     print(*cost)


# ver 3
# n = int(input())
# m = int(input())
# costs = [[0] * n for _ in range(n)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     if costs[a][b]:
#         costs[a][b] = min(costs[a][b], c)
#     else:
#         costs[a][b] = c
#
#
# def unknown_way(start, to, now, cost):
#     pass
#
#
# def known_way(start, to, now, cost):
#     pass
#
#
#
# visited = [0] * n
# for i in range(n):
#     for j in range(i):
#         known_way(i, j)
#
#     for j in range(i+1, n):
#         pass
