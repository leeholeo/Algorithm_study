N, L = map(int, input().split())
pools = [tuple(map(int, input().split())) for _ in range(N)]
pools.sort()
covered = 0
result = 0
for l, right in pools:
    left = max(covered, l)
    if left >= right:
        continue

    share, remainder = divmod(right - left, L)
    if remainder:
        covered = right + L - remainder
        result += share + 1
    else:
        covered = right
        result += share

print(result)
