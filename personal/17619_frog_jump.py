import sys


input = sys.stdin.readline
N, Q = map(int, input().split())
logs = []
for i in range(1, N + 1):
    x1, x2, __ = map(int, input().split())
    logs.append((x1, x2, i))

logs_sorted = sorted(logs)
logs = [None] + logs
last_right = -1
cnt = 0
for left, right, idx in logs_sorted:
    if left > last_right:
        cnt += 1

    logs[idx] = cnt
    last_right = max(last_right, right)

for _ in range(Q):
    l1, l2 = map(int, input().split())
    if logs[l1] == logs[l2]:
        print(1)
    else:
        print(0)
