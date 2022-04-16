n = int(input())
a, b, c = 0, 0, 0
for _ in range(n):
    wine = int(input())
    a, b, c = b + wine, c + wine, max(a, b, c)

print(max(a, b, c))
