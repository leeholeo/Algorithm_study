N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    f, t, c = map(int, input().split())
    if f > D or t > D:
        continue

    shortcuts.append((f, t, c))
checkpoints = set()
for f, t, c in shortcuts:
    checkpoints.update((f, t))

checkpoints = list(checkpoints)
checkpoints.sort()
len_check = len(checkpoints)
destinations = [[] for _ in range(len_check)]
checkpoints.append(D)
dp = [9876543210] * (len_check+1)
conversion = {}
for i in range(len_check):
    conversion[checkpoints[i]] = i

for f, t, c in shortcuts:
    f_convert = conversion[f]
    t_convert = conversion[t]
    destinations[f_convert].append((t_convert, c))

dp[0] = checkpoints[0]
for i in range(len_check):
    dp[i+1] = min(dp[i+1], dp[i] + checkpoints[i+1] - checkpoints[i])
    for t, c in destinations[i]:
        dp[t] = min(dp[t], dp[i] + c)

print(dp[-1])
