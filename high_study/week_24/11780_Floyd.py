import sys


input = sys.stdin.readline
n = int(input())
m = int(input())
costs = [[0] * (n+1) for _ in range(n+1)]
ways = [[[] for _ in range(n+1)] for __ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(c, costs[a][b]) if costs[a][b] else c
    ways[a][b] = [a]

for waypoint in range(1, n+1):
    for start in range(1, n+1):
        for destin in range(1, n+1):
            s_w = costs[start][waypoint]
            w_d = costs[waypoint][destin]
            s_d = costs[start][destin]
            if s_w == 0 or w_d == 0:
                continue
            if s_d == 0 or s_w + w_d < s_d:
                costs[start][destin] = s_w + w_d
                ways[start][destin] = ways[start][waypoint] + ways[waypoint][destin]
for k in range(1, n+1):
    costs[k][k] = 0
    ways[k][k] = []

for row in range(1, n+1):
    for col in range(1, n+1):
        print(costs[row][col], end=' ')
    print()

for row in range(1, n+1):
    for col in range(1, n+1):
        if ways[row][col]:
            print(len(ways[row][col])+1, *ways[row][col], col)
        else:
            print(0)
