N = int(input())
children = [[] for _ in range(N)]
children_input = map(int, input().split())
delete_node = int(input())
stack = [delete_node]
for child, parent in enumerate(children_input):
    if parent == -1:
        continue

    if child == delete_node:
        continue

    children[parent].append(child)

while stack:
    now = stack.pop()
    if not children[now]:
        children[now].append(-1)
        continue

    stack.extend(children[now])

cnt = 0
for i in range(N):
    if not children[i]:
        cnt += 1

print(cnt)
