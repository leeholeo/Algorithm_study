n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
distances = []


def distance(s1, s2):
    dx = abs(stars[s1][0] - stars[s2][0])
    dy = abs(stars[s1][1] - stars[s2][1])
    dist = (dx**2 + dy**2) ** 0.5
    return dist


for star1 in range(n-1):
    for star2 in range(star1+1, n):
        distances.append((distance(star1, star2), star1, star2))
distances.sort()
parents = [False] * n


def find(c):
    if parents[c] is not False:
        parent_c = find(parents[c])
        parents[c] = parent_c
        return parent_c
    else:
        return c


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return False
    else:
        parents[parent_b] = parent_a
        return True


result = 0
length = len(distances)
for edge in range(length):
    dist, star1, star2 = distances[edge]
    if union(star1, star2):
        result += dist

print(f'{result:.2f}')
