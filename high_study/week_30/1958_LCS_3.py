strings = [input() for _ in range(3)]
dp = [[[0] * (len(strings[2])+1) for _ in range(len(strings[1])+1)] for __ in range(len(strings[0])+1)]
for i in range(1, len(strings[0])+1):
    for j in range(1, len(strings[1])+1):
        for k in range(1, len(strings[2])+1):
            if strings[0][i-1] == strings[1][j-1] == strings[2][k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[i][j][k])
