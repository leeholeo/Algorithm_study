"""
마지막 숫자(0 혹은 1)와 수열 길이, 그리고 인접한 비트의 개수의 세 가지 요소로 dp
"""
N_LIMIT = 101
K_LIMIT = N_LIMIT
END_0 = 0
END_1 = 1

T = int(input())
dp = [[[0] * N_LIMIT for _ in range(K_LIMIT)] for __ in range(2)]
dp[END_0][0][0] = 1
dp[END_1][0][0] = 1
for bit_idx in range(N_LIMIT-1):
    for k_idx in range(bit_idx+1):
        dp[END_0][bit_idx+1][k_idx] += dp[END_0][bit_idx][k_idx]
        dp[END_1][bit_idx+1][k_idx] += dp[END_0][bit_idx][k_idx]
        dp[END_0][bit_idx+1][k_idx] += dp[END_1][bit_idx][k_idx]
        dp[END_1][bit_idx+1][k_idx+1] += dp[END_1][bit_idx][k_idx]

for _ in range(T):
    n, k = map(int, input().split())
    print(dp[END_0][n-1][k] + dp[END_1][n-1][k])
