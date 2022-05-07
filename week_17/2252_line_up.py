from collections import deque


# idx -> value 순으로 간선을 기록한 edges와 value -> idx 순으로 간선을 기록한 priorities 인접 리스트
N, M = map(int, input().split())
priorities = [[] for _ in range(N+1)]
# priorities = [0] * (N+1)
edges = [[] for _ in range(N+1)]
for _ in range(M):
    front, rear = map(int, input().split())
    edges[front].append(rear)
    priorities[rear].append(front)
    # priorities[rear] += 1

# 이번에 제거할 정점을 보관하는 queue 생성
queue = deque()
for node in range(1, N+1):
    if priorities[node]:
        continue
    queue.append(node)

# Kahn's algorithm
answer = []
while queue:
    now_node = queue.popleft()
    answer.append(now_node)
    for next_node in edges[now_node]:
        # priorities에서 이번 정점을 찾아서 제거
        index_of_now_node = priorities[next_node].index(now_node)
        priorities[next_node].pop(index_of_now_node)
        # priorities[next_node].pop()
        # priorities[next_node] -= 1
        # priorities[node]를 모두 출력 후, 즉 priorities[node] == []면 node 출력 가능
        if not priorities[next_node]:
            queue.append(next_node)

if len(answer) == N:
    print(*answer)
else:
    print("It is not DAU(Directed Acyclic Graph)")
