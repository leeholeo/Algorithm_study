'''
dp
1. 길이 n, l개의 1을 쓰든지 말든지 알아서 하는 dp
2. 길이 n, l개의 1을 다 쓸 때의 dp
'''
N, L, I = map(int, input().split())
dp = [[0] * (N+1) for _ in range(L+1)]
for j in range(N+1):
    dp[0][j] = 1
for i in range(1, L+1):
    dp[i][i] = 1
for i in range(1, L+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

i = L
j = N
cnt = I
answer = ''
while j >= 1:
    j -= 1
    if cnt > dp[i][j]:
        answer += '1'
        cnt -= dp[i][j]
        i -= 1
    else:
        answer += '0'
print(answer)
