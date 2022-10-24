'''
lazy propagation
'''
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(map(int, input().split()))
parent = [None] + parent
praise = [0] * (n+1)
for _ in range(m):
    i, w = map(int, input().split())
    praise[i] += w

for i in range(2, n+1):
    praise[i] += praise[parent[i]]
print(*praise[1:])
