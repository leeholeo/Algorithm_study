def dfs(v):
    now = v
    idx = len(tree[now]) - 1
    visited = [False] * (N+1)
    visited[now] = True
    stack = []
    print(now, end=' ')
    while True:
        if idx < 0:
            try:
                now, idx = stack.pop()
                continue
            except IndexError:
                break

        nxt = tree[now][idx]
        if visited[nxt]:
            idx -= 1
        else:
            stack.append((now, idx-1))
            visited[nxt] = True
            print(nxt, end=' ')
            now, idx = nxt, len(tree[nxt]) - 1

    print()


def bfs(v):
    visited = [False] * (N+1)
    queue = [None] * (N+1)
    queue[0] = v
    front = 0
    rear = 1
    while front != rear:
        now = queue[front]
        front += 1
        visited[now] = True
        print(now, end=' ')

        for nxt in tree[now]:
            if visited[nxt]:
                continue

            queue[rear] = nxt
            rear += 1
            visited[nxt] = True


N, M, V = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(N+1):
    tree[i].sort(reverse=True)

dfs(V)
for i in range(N+1):
    tree[i] = reversed(tree[i])

bfs(V)
