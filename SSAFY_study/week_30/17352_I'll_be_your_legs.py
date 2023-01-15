'''
union find
'''
import sys
input = sys.stdin.readline


def find(child):
    if bridges[child] is None:
        return child
    return find(bridges[child])


def union(a, b):
    pa, pb = find(a), find(b)
    mini = min(pa, pb)
    maxi = max(pa, pb)
    bridges[maxi] = mini


N = int(input())
bridges = [None] * N
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a-1, b-1)

ans = []
for i in range(N):
    if bridges[i] is None:
        ans.append(i+1)

print(*ans)
