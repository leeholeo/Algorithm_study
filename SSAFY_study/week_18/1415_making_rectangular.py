'''
brute-force
십자로 자르고 두개씩 합치는 방법이 훨씬 쉬울 것으로 예상됨
'''
def area(t, l, b, r):
    return rec_sum[b][r] - rec_sum[b][l-1] - rec_sum[t-1][r] + rec_sum[t-1][l-1]


N, M = map(int, input().split())
rec = [list(map(int, list(input()))) for _ in range(N)]
rec_sum = [[0] * (M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        rec_sum[i][j] = rec[i][j] + rec_sum[i-1][j] + rec_sum[i][j-1] - rec_sum[i-1][j-1]

max_mul = 0
for i in range(N-1):
    for j in range(M-1):
        max_mul = max(max_mul, area(0, 0, i, M-1) * area(i+1, 0, N-1, j) * area(i+1, j+1, N-1, M-1))
for i in range(N-1):
    for j in range(M-1):
        max_mul = max(max_mul, area(0, 0, i, j) * area(0, j+1, i, M-1) * area(i+1, 0, N-1, M-1))
for i in range(N-1):
    for j in range(M-1):
        max_mul = max(max_mul, area(0, 0, N-1, j) * area(0, j+1, i, M-1) * area(i+1, j+1, N-1, M-1))
for i in range(N-1):
    for j in range(M-1):
        max_mul = max(max_mul, area(0, 0, i, j) * area(i+1, 0, N-1, j) * area(0, j+1, N-1, M-1))

for i in range(N-2):
    for j in range(i+1, N-1):
        max_mul = max(max_mul, area(0, 0, i, M-1) * area(i+1, 0, j, M-1) * area(j+1, 0, N-1, M-1))
for i in range(M-2):
    for j in range(i+1, M-1):
        max_mul = max(max_mul, area(0, 0, N-1, i) * area(0, i+1, N-1, j) * area(0, j+1, N-1, M-1))

print(max_mul)

