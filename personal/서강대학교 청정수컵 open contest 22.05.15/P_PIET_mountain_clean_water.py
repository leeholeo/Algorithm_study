N = int(input())
hikers = []
for _ in range(N):
    p_i, c_i = map(int, input().split())
    hikers.append((c_i, p_i))

hikers.sort()
dp = [0] * (N * 100 + 1)
dp[0] = 1

for c_i, p_i in hikers:
    for i in range(c_i-1, -1, -1):
        if dp[i]:
            dp[i+p_i] = max(dp[i+p_i], dp[i]+1)

maxi = 0
mini_idx = 0
for i in range(min(len(dp), 3200)):
    if dp[i] > maxi:
        maxi = dp[i]
        mini_idx = i

print(maxi-1, mini_idx)
