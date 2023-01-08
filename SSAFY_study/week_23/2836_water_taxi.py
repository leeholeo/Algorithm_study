'''
greedy
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
people = []
for _ in range(N):
    f, t = map(int, input().split())
    if t >= f:
        continue
    people.append((t, f))
people.sort()
people.append((M+1, M+1))
l = 0
r = 0
answer = 0
for t, f in people:
    if r < t:
        answer += r-l
        r = f
        l = t
    else:
        r = max(r, f)
print(2*answer + M)