'''
이호형
backtracking
5초
일반적인 backtracking dfs로는 시간초과
체스판을 45도 회전시켜 다이아 모양의 체스판에서, n-rook문제로 변형
'''
# import sys
# import time
#
#
# def output():
#     print(maxi)
#
#
# # dfs
# def dfs(diag_depth, cnt):
#     global maxi
#     # 종료조건
#     if diag_depth == length:
#         maxi = max(maxi, cnt)
#         # 최대값이면
#         if maxi == length:
#             output()
#             print(3, time.time() - start_time)
#             exit()
#     # pruning
#     if maxi - cnt >= length - diag_depth:
#         return
#
#     # backtracking
#     for right_down in possible_position[diag_depth]:
#         if visited[right_down]:
#             visited[right_down] = False
#             dfs(diag_depth+1, cnt+1)
#             visited[right_down] = True
#     dfs(diag_depth+1, cnt)
#
#
# # input
# size = int(input())
# chess = [sys.stdin.readline().split() for _ in range(size)]
# start_time = time.time()
# # 체스판을 45도 돌려 n-rook 문제로 변환
# # possible_position: /축 좌표가 idx, [\축 좌표...]가 value
# # visited: \축 좌표가 idx, 방문했다면 False
# length = 2*size - 1
# possible_position = [[] for _ in range(length)]
# visited = [True] * length
# for i in range(size):
#     for j in range(size):
#         if chess[i][j] == '1':
#             possible_position[i+j].append(i-j)
# # dfs
# maxi = 0
# print(1, time.time() - start_time)
# dfs(0, 0)
# output()
# print(2, time.time() - start_time)
'''
hello70825님의 풀이
56ms
n-rook 문제로 변환하는 부분은 같고, 일정 부분 복잡하기까지 하다.
left와 right는 각각 /축과 \축의 방문 배열이다.
속도적인 측면에서 크게 차이가 나는 부분은 dfs 부분이다.
한 축을 순회하면서 반대축을 기준으로 빈 곳에 배치하는 방식
만약 한 축에서 놓을 수 있는 반대축 목록(path)에서 모든 반대축에 비숍이 배치됐다면,
배치된 비숍의 축 좌표를 left와 right에서 찾은 후 dfs를 재귀 호출한다.
dfs를 재귀호출하면 이전에 놓았던 축에서 반대축 목록을 탐색하고 빈 반대축이 있다면 비숍을 해당 위치로 이동한다.
무한루프를 막기 위해 축이 idx가 되는 방문 배열 visited를 사용한다.
'''
# def dfs(x):
#     visited[x]=1
#     for nx in path[x]:
#         if left[nx]==-1 or (not visited[left[nx]] and dfs(left[nx])):
#             right[x]=nx
#             left[nx]=x
#             return 1
#     return 0
# n=int(input())
# D=[[*map(int,input().split())] for _ in range(n)]
# start_time = time.time()
# R=[[-1]*n for _ in range(n)]
# L=[[-1]*n for _ in range(n)]
# r,l=-1,-1
# for i in range(n):
#     r+=1
#     x,y=0,i
#     for j in range(n-1-i,-1,-1):
#         if D[x][y]==1:R[x][y]=r
#         x+=1;y+=1
# for i in range(1,n):
#     r+=1
#     x,y=i,0
#     for j in range(n-i-1,-1,-1):
#         if D[x][y]==1:R[x][y]=r
#         x+=1;y+=1
# for i in range(n):
#     l+=1
#     x,y=0,i
#     for j in range(n):
#         if D[x][y]==1:L[x][y]=l
#         x+=1;y-=1
# for i in range(1,n):
#     l+=1
#     x,y=i,n-1
#     for j in range(n-1-i,-1,-1):
#         if D[x][y]==1:L[x][y]=l
#         x+=1;y-=1
# r+=1;l+=1
# path=[[] for _ in range(r)]
# for i in range(n):
#     for j in range(n):
#         if R[i][j]>=0 and L[i][j]>=0:
#             path[R[i][j]].append(L[i][j])
# right=[-1]*r
# left=[-1]*l
# res=0
# print(4, time.time() - start_time)
# for i in range(r):
#     if right[i]==-1:
#         visited=[0]*r
#         if dfs(i):res+=1
# print(res)
# print(5, time.time() - start_time)
