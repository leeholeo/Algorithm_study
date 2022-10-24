N = int(input())
red, green, blue = 0, 0, 0
for _ in range(N):
    r, g, b = map(int, input().split())
    red, green, blue = min(green + r, blue + r), min(red + g, blue + g), min(red + b, green + b)

print(min(red, green, blue))
