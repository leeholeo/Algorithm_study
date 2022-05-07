N, M = map(int, input().split())
benefits = [[0] * M] + [list(map(int, input().split()))[1:] for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]
logs = [[[] for _ in range(M+1)] for __ in range(N+1)]
for i in range(M+1):
    logs[0][i] = [0] * i

for corpor in range(M):
    for accum_cost in range(N+1):
        for cost in range(N+1-accum_cost):
            next_bene = dp[accum_cost][corpor] + benefits[cost][corpor]
            if next_bene > dp[accum_cost+cost][corpor+1]:
                dp[accum_cost+cost][corpor+1] = next_bene
                logs[accum_cost+cost][corpor+1] = logs[accum_cost][corpor] + [cost]

max_bene_cost = 0
max_bene = 0
for cost in range(N+1):
    if dp[cost][-1] > max_bene:
        max_bene = dp[cost][-1]
        max_bene_cost = cost

print(max_bene)
print(*logs[max_bene_cost][-1])
