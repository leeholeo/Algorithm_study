import sys


def making_square(n, m):
    for r in range(1, n):
        dp[r][1] = r

    for c in range(1, m):
        dp[1][c] = c

    for diag in range(2, m):
        dp[diag][diag] = 1

    for r in range(3, m):
        for c in range(2, r):
            # if r % c:
            #     dp[r][c] = r // c
            #     continue
            dp[r][c] = min(dp_r(r, c), dp_c(r, c))
            dp[c][r] = dp[r][c]

    if n <= 250:
        for r in range(m, n):
            for c in range(2, m):
                # if r % c:
                #     dp[r][c] = r // c
                #     continue
                dp[r][c] = min(dp_r(r, c), dp_c(r, c))
    else:
        for r in range(m, 250):
            for c in range(2, m):
                # if r % c:
                #     dp[r][c] = r // c
                #     continue
                dp[r][c] = min(dp_r(r, c), dp_c(r, c))

        for r in range(250, n):
            # if r % c:
            #     dp[r][c] = r // c
            #     continue
            dp[r][m-1] = dp_c(r, m-1)


def dp_r(r, c):
    cut = c // 2
    mini = dp[r][1] + dp[r][c-1]
    for side in range(2, cut+1):
        mini = min(mini, dp[r][side] + dp[r][c-side])

    return mini


def dp_c(r, c):
    cut = r // 2
    mini = dp[1][c] + dp[r-1][c]
    for side in range(2, cut+1):
        mini = min(mini, dp[side][c] + dp[r-side][c])

    return mini


n, m = map(int, sys.stdin.readline().split())
if m > n:
    n, m = m, n
dp = [[0] * (m + 1) for _ in range(n+1)]
making_square(n+1, m+1)
print(dp[n][m])
