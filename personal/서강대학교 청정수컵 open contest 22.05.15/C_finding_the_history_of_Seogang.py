N, M = map(int, input().split())
now = list(map(int, input().split()))
past = list(map(int, input().split()))
if N < M:
    now += [0] * (M-N)
maxi = 0
for i in range(M):
    maxi = max(maxi, past[i]-now[i])

print(maxi)
