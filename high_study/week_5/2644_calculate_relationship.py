def calculate_relationship():
    def find(node):
        parents_node = []
        while True:
            parents_node.append(node)
            if parents[node] == 0:
                break

            node = parents[node]

        return parents_node

    parents_a = find(a)
    parents_b = find(b)
    len_a = len(parents_a)
    len_b = len(parents_b)
    i = -1
    for _ in range(min(len_a, len_b)):
        if parents_a[i] != parents_b[i]:
            if i == -1:
                return -1

            break

        i -= 1

    return len_a + len_b + 2 * (i + 1)


n = int(input())
parents = [0] * (n+1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    parents[y] = x

print(calculate_relationship())
