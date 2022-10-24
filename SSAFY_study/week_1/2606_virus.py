# N = int(input())
# num = int(input())
# virus = [[] for _ in range(N+1)]
# for _ in range(num):
#     a, b = map(int, input().split())
#     virus[a].append(b)
#     virus[b].append(a)
# q = [1]
# visited = [0] * (N+1)
# cnt = 0
# while q:
#     now = q.pop(0)
#     if visited[now]:
#         continue
#     else:
#         cnt += 1
#         visited[now] = 1
#         for i in virus[now]:
#             q.append(i)
#
# print(cnt-1)

import sys
_=input();T={};V=[0]*101
def D(k):
 while T[k]:
  t=T[k].pop()
  if not V[t]:V[t]=1;D(t)
A={(*map(int,sys.stdin.readline().split()),) for i in range(int(input()))}
for a in A:
 for i in [0,1]:T.setdefault(a[i],[]).append(a[1-i])
D(1)
print(sum(V[2:]))
