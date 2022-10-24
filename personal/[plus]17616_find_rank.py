# sys input은 체고시다...
# dfs로도 풀어보고 속도를 비교해보자. bfs가 빠를 것 같다.


# bfs
# from collections import deque
# import sys
#
#
# def find_rank(x):

#     q_up = deque()
#     q_down = deque()
#
#     q_up.append(x)
#     q_down.append(x)
#
#     def bfs(rank, q):
#         cnt = 0
#         visited = [False] * (N + 1)
#         visited[x] = True
#         while True:
#             try:
#                 now = q.popleft()
#                 for vertex in rank[now]:
#                     if not visited[vertex]:
#                         q.append(vertex)
#                         cnt += 1
#                         visited[vertex] = True
#             except IndexError:
#                 return cnt
#
#     return bfs(uprank, q_up) + 1, N - bfs(downrank, q_down)
#
#
# N, M, X = map(int, input().split())
# uprank = [[] for _ in range(N + 1)]
# downrank = [[] for _ in range(N + 1)]
# for _ in range(M):
#     A, B = map(int, sys.stdin.readline().split())
#     uprank[B].append(A)
#     downrank[A].append(B)
#
# print(' '.join(map(str, find_rank(X))))


# dfs
import sys


def find_rank(x):
    stack_up = [0] * (min(N, M) + 10)
    stack_down = [0] * (min(N, M) + 10)

    def push(s, thing, top):
        top += 1
        s[top] = thing

    def p0p(s, top):
        rtn = s[top]
        top -= 1
        return rtn

    def dfs(rank, s):
        top = -1
        cnt = 0
        visited = [0] * (N + 1)
        now = [x, -1]

        while True:
            try:
                for i in range(now[1] + 1, len(rank[now[0]])):
                    if visited[rank[now[0]][i]]:
                        continue
                    push(s, [now[0], i], top)
                    now = [rank[now[0]][i], -1]
                    visited[now[0]] = 1
                    cnt += 1
                    break
                else:
                    now = p0p(s, top)
            except TypeError:
                return cnt

    return dfs(uprank, stack_up) + 1, N - dfs(downrank, stack_down)


N, M, X = map(int, input().split())
uprank = [[] for _ in range(N + 1)]
downrank = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    uprank[B].append(A)
    downrank[A].append(B)

print(' '.join(map(str, find_rank(X))))
