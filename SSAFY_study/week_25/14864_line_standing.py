'''
simple topological sort
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
parent = [0]*(N+1)
child = [0]*(N+1)
for _ in range(M):
    X, Y = map(int, input().split())
    parent[X] += 1
    child[Y] += 1

for i in range(1, N+1):
    parent[i] += i - child[i]
if len(parent) == len(set(parent)):
    print(*parent[1:])
else:
    print(-1)
