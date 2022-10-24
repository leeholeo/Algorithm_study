'''
dp[지각을 했냐 안 했냐][결석이 몇 스택이냐][며칠째냐]
다 풀어놓고 보니까
dp[며칠째냐][지각을 했냐 안 했냐][결석이 몇 스택이냐]
형태가 나아 보임
'''


n = int(input())
dp = [[[0] * n for _ in range(3)] for __ in range(2)]
LATE_0 = 1
LATE_1 = 0
ABSENT_0 = 0
ABSENT_1 = 1
ABSENT_2 = 2
dp[LATE_0][ABSENT_0][0] = 1
dp[LATE_0][ABSENT_1][0] = 1
dp[LATE_1][ABSENT_0][0] = 1
for i in range(n - 1):
    for late in (LATE_0, LATE_1):
        for absent in (ABSENT_0, ABSENT_1, ABSENT_2):
            dp[late][ABSENT_0][i+1] += dp[late][absent][i]
    for late in (LATE_0, LATE_1):
        for absent in (ABSENT_0, ABSENT_1):
            dp[late][absent+1][i+1] += dp[late][absent][i]
    for absent in (ABSENT_0, ABSENT_1, ABSENT_2):
        dp[LATE_1][ABSENT_0][i+1] += dp[LATE_0][absent][i]

total = 0
for late in (LATE_0, LATE_1):
    for absent in (ABSENT_0, ABSENT_1, ABSENT_2):
        total += dp[late][absent][n-1]
print(total % 1000000)
