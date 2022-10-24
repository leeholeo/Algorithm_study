def find(c):
    if parents[c] is None:
        return c

    parents[c] = find(parents[c])
    return parents[c]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parents[pb] = pa


N = int(input())
M = int(input())
ways = [list(map(int, input().split())) for _ in range(N)]
plan_cities = list(map(lambda x: int(x)-1, input().split()))
parents = [None] * N
for i in range(N):
    for j in range(i+1, N):
        if ways[i][j]:
            union(i, j)

p = find(plan_cities[0])
for city in plan_cities:
    if p != find(city):
        print('NO')
        break
else:
    print('YES')
