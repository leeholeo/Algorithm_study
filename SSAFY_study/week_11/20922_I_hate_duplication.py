'''
투포인터
'''
LIMIT = 100001
N, K = map(int, input().split())
sequence = list(map(int, input().split()))
a = [0] * LIMIT
max_length = 0
left, right = 0, 0
while right < N:
    now = sequence[right]
    if a[now] == K:
        max_length = max(max_length, right - left)
        while a[now] == K:
            oldest = sequence[left]
            a[oldest] -= 1
            left += 1
    a[now] += 1
    right += 1
max_length = max(max_length, right-left)
print(max_length)
