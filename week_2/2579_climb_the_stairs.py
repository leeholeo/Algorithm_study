n = int(input())
stairs = (0, *map(int, [input() for _ in range(n)]))
try:
    dp = []
    dp.append((0, 0))  # dp.append((0, None))
    dp.append((stairs[1], 0))  # dp.append((stairs[1], None))
    dp.append((stairs[2], dp[1][0]+stairs[2]))  # dp.append((stairs[2], None))
    dp.append((dp[1][0]+stairs[3], dp[2][0]+stairs[3]))
    dp.extend([[0, 0] for _ in range(n-3)])
    stairs[4]
    for i in range(4, n+1):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
        dp[i][1] = dp[i-1][0] + stairs[i]

    print(max(dp[n][0], dp[n][1]))
except IndexError:
    print(max(dp[n][0], dp[n][1]))
