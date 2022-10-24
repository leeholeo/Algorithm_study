import sys


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
    length = len(heap)
    temp = 0
    while temp != -1:
        now = temp
        temp = -1
        cv1 = now * 2 + 1
        cv2 = now * 2 + 2
        if cv2 < length:
            smaller = cv1 if heap[cv1] <= heap[cv2] else cv2
            if heap[now] > heap[smaller]:
                heap[now], heap[smaller] = heap[smaller], heap[now]
                temp = smaller
        elif cv1 < length:
            if heap[now] > heap[cv1]:
                heap[now], heap[cv1] = heap[cv1], heap[now]

            break
        else:
            break

    return rtn


input = sys.stdin.readline
N = int(input())
M = int(input())
buses = [{} for _ in range(N+1)]
costs = [987654321] * (N+1)
h = []
for _ in range(M):
    a, b, c = map(int, input().split())
    buses[a][b] = min(buses[a].get(b, 987654321), c)

frm, to = map(int, input().split())
costs[frm] = 0
heap_push(h, (costs[frm], frm))

while h:
    cost, now = heap_pop(h)
    for nxt, c in buses[now].items():
        next_cost = cost + c
        if next_cost < costs[nxt]:
            costs[nxt] = next_cost
            heap_push(h, (costs[nxt], nxt))

print(costs[to])

# # 용우 플로이드 응용 / 실패
# import sys
#
#
# input = sys.stdin.readline
# n, m = int(input()), int(input())
# city = [[float('inf')] * n for _ in range(n)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     a, b = a - 1, b - 1
#     city[a][b] = min(c, city[a][b])
#
# for i in range(n):
#     city[i][i] = 0
#
# frm, to = map(int, input().split())
# frm, to = frm - 1, to - 1
#
# for j in range(n):
#     for k in range(n):
#         if j == k or k == frm:
#             continue
#         city[frm][j] = min(city[frm][j], city[frm][k] + city[k][j])
#
# print(city[frm][to])
