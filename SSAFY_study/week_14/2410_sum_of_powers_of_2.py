'''
삽질 오지게 하다가 다른 풀이 확인함
dp를 왜 top-down으로 접근했는지 모르겠다.
dp는 무조건 bottom-up이 맞는듯?
dp 방법
    1. 2**n 을 하나씩 추가해가며 조합 찾기(해당 풀이)
    2. 2가 0개인 경우(//2) + 2가 1개 이상인 경우(-2), 더 효율적
'''
import sys


input = sys.stdin.readline
N = int(input())
dp = [1] * (N+1)
power = 1
for i in range(N):
    power = power << 1
    if power > N:
        break
    for j in range(power, N+1):
        dp[j] += dp[j-power]
        dp[j] %= 1000000000
print(dp[-1])
