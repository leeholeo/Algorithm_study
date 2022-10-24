D1, D3, D5 = 10000, 25000, 37000
N, M = map(int, input().split())
schedule = [1] * (N+1)
dp = [dict() for _ in range(N+5)]
if M != 0:
    for day in map(int, input().split()):
        schedule[day] = 0

mini = 1000000
dp[0] = {0: 0}
for d in range(N):
    if schedule[d+1] == 0:
        for key, item in dp[d].items():
            dp[d+1][key] = min(dp[d+1].get(key, mini), dp[d][key])

    else:
        for key, item in dp[d].items():
            if key >= 3:
                dp[d + 1][key-3] = min(dp[d + 1].get(key-3, mini), dp[d][key])
            else:
                dp[d+1][key] = min(dp[d+1].get(key, mini), dp[d][key]+D1)

            dp[d+3][key+1] = min(dp[d+3].get(key+1, mini), dp[d][key]+D3)
            dp[d+5][key+2] = min(dp[d+5].get(key+2, mini), dp[d][key]+D5)

for d in range(N, N+5):
    for value in dp[d].values():
        mini = min(mini, value)

print(mini)
