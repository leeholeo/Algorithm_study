h, w = map(int, input().split())
figures = [input() for _ in range(h)]
figures_area = [[0] * w for _ in range(h)]
for k in range(h + w):
    inner = False
    for i in range(max(0, k - w + 1), min(h, k + 1)):
        if figures[i][k - i] == '\\':
            inner = not inner
            figures_area[i][k - i] = 1
            continue

        if inner:
            figures_area[i][k - i] = 2

for k in range(-h, w - 1):
    inner = False
    for i in range(max(0, -k), min(h, w - k)):
        if figures[i][k + i] == '/':
            inner = not inner
            figures_area[i][k + i] = 1
            continue

        if inner:
            figures_area[i][k + i] = 2

result = 0
for area in figures_area:
    result += sum(area)

print(result // 2)
