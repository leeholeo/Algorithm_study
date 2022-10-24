# bfs union
import sys
from collections import deque


def civilize(q):
    linked = 1
    united = [[0] * (N + 1) for _ in range(N + 1)]
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while True:
        while q:
            x, y = q.popleft()
            root = world[x][y]
            for drc in directions:
                nx, ny = x + drc[0], y + drc[1]
                if nx < 1 or ny < 1:
                    continue

                try:
                    nroot = world[nx][ny]
                except IndexError:
                    continue

                root_p = (root[0], root[1], root[2] + 1)
                if nroot:
                    root2 = (root[0], root[1])
                    nroot2 = (nroot[0], nroot[1])
                    if nroot2 < root2:
                        if united[root[0]][root[1]]:
                            continue

                        world[x][y] = nroot
                        linked += 1
                        united[root[0]][root[1]] = nroot
                    elif root2 < nroot2:
                        if united[nroot[0]][nroot[1]]:
                            continue

                        world[nx][ny] = root
                        linked += 1
                        united[nroot[0]][nroot[1]] = root

                    if linked == K:
                        return nroot[2]

                else:
                    world[nx][ny] = root_p
                    q.append((nx, ny))


N, K = map(int, sys.stdin.readline().split())
world = [[0] * (N + 1) for _ in range(N + 1)]
queue = deque()
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    world[x][y] = (x, y, 0)
    queue.append((x, y))

print(civilize(queue))

# # MST
# import heapq
# N, K = map(int, input().split())
# civilization = [tuple(map(int, input().split())) for _ in range(K)]
# # 1. sort
# civilization.sort()
# # 2. not sort
# linked = 1
# now = civilization[0]
# years = heapq()
# while linked < K:
#