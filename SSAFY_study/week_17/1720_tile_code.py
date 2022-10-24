'''
또p
'''
N = int(input())
dp = [0] * (N+2)
dp[0] = 1
for i in range(N):
    dp[i+1] += dp[i]
    dp[i+2] += 2 * dp[i]
result = dp[N] + dp[N//2]
if N % 2 == 0:
    result += 2 * dp[N//2-1]
print(result//2)
