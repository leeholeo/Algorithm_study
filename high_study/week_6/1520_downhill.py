# dp
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


M, N = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(M)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
dp = [[0] * N for _ in range(M)]
dp[M-1][N-1] = 1
h = [(fields[M-1][N-1], M-1, N-1)]
while h:
    _, x, y = heap_pop(h)
    if x == 0 and y == 0:
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < M and 0 <= ny < N):
            continue

        if fields[x][y] >= fields[nx][ny]:
            continue

        if not dp[nx][ny]:
            heap_push(h, (fields[nx][ny], nx, ny))

        dp[nx][ny] += dp[x][y]

print(dp[0][0])


# # dfs 시간초과
# def dfs(x, y):
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if not (0 <= nx < M and 0 <= ny < N):
#             continue
#
#         if fields[x][y] <= fields[nx][ny]:
#             continue
#
#         if nx == M - 1 and ny == N - 1:
#             global route
#             route += 1
#             continue
#
#         dfs(nx, ny)
#
#
# M, N = map(int, input().split())
# fields = [list(map(int, input().split())) for _ in range(M)]
# directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
# route = 0
# dfs(0, 0)
#
# print(route)
