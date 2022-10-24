'''
dp[n_idx][n_idx 번째가 포함되었는지][구간의 갯수]
포함 -> 포함
포함 -> 미포함
미포함 -> 포함(구간 갯수 증가)
미포함 -> 미포함
'''
OUT = 0 # 미포함
IN = 1  # 포함
BOTTOM = -9876543210    # 초기화 값
N, M = map(int, input().split())
sequence = [int(input()) for _ in range(N)]
dp = [[[BOTTOM] * (M+2) for _ in range(2)] for __ in range(N)]
dp[0][IN][1] = sequence[0]
dp[0][OUT][0] = 0
# sequence idx
for i in range(N-1):
    # 구간의 수
    for j in range(M+1):
        # 값이 존재하면
        if dp[i][IN][j] != BOTTOM:
            dp[i+1][IN][j] = max(dp[i][IN][j] + sequence[i+1], dp[i+1][IN][j])
            dp[i+1][OUT][j] = max(dp[i][IN][j], dp[i+1][OUT][j])
        if dp[i][OUT][j] != BOTTOM:
            dp[i+1][IN][j+1] = max(dp[i][OUT][j] + sequence[i+1], dp[i+1][IN][j+1])
            dp[i+1][OUT][j] = max(dp[i][OUT][j], dp[i+1][OUT][j])
        # 특정 구간의 수에서 미포함 상태에 값이 없다는 것은 더 큰 구간의 수에서 값이 존재하지 않음
        else:
            break
answer = BOTTOM
for io in (IN, OUT):
    answer = max(answer, dp[-1][io][M])
print(answer)
