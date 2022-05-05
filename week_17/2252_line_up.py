from collections import deque


N, M = map(int, input().split())
priorities = [[] for _ in range(N+1)]
# priorities = [0] * (N+1)
edges = [[] for _ in range(N+1)]
for _ in range(M):
    # priorities[node]를 모두 출력 후 node 출력 가능
    front, rear = map(int, input().split())
    edges[front].append(rear)
    priorities[rear].append(front)
    # priorities[rear] += 1

queue = deque()
for node in range(1, N+1):
    if priorities[node]:
        continue
    queue.append(node)

answer = []
while queue:
    now_node = queue.popleft()
    answer.append(now_node)
    for next_node in edges[now_node]:
        index_of_now_node = priorities[next_node].index(now_node)
        priorities[next_node].pop(index_of_now_node)
        # priorities[next_node].pop()
        # priorities[next_node] -= 1
        if not priorities[next_node]:
            queue.append(next_node)

if len(answer) == N:
    print(*answer)
else:
    print("It is not DAU(Directed Acyclic Graph)")
