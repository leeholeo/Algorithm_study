'''
dp
'''
import sys


input = sys.stdin.readline
LIMIT = 9876543210
n, m = map(int, input().split())
name = [int(input()) for _ in range(n)]
dp = [LIMIT] * n + [0]
for i in range(n):
    cnt = 0
    length = name[i]
    while length <= m:
        if i+cnt == n-1:
            dp[i+cnt] = min(dp[i+cnt], dp[i-1])
        else:
            dp[i+cnt] = min(dp[i+cnt], dp[i-1] + (m-length)**2)
        cnt += 1
        if i + cnt >= n:
            break
        length += name[i+cnt] + 1
print(dp[-2])
