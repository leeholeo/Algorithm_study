strings = [input() for _ in range(2)]
dp = [[0] * (len(strings[1])+1) for __ in range(len(strings[0])+1)]
for i in range(1, len(strings[0])+1):
    for j in range(1, len(strings[1])+1):
        if strings[0][i-1] == strings[1][j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[i][j])
