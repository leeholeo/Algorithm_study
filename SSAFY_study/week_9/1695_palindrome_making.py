'''
모르겠어서 알고리즘 분류로 dp라는 걸 확인하고 시도
왼쪽과 오른쪽을 각각 얼마만큼 palindrome 처리했는가(더이상 신경쓰지 않아도 됨)를 기준으로 dp
2차원 dp를 사용, row idx가 왼쪽, col idx이 오른쪽에서 처리한 수의 갯수(반대도 상관은없음)
dp 내에 들어가는 값은 끼워 넣은 수의 갯수
python에서는 메모리 초과, pypy에서는 통과
'''
import sys


input = sys.stdin.readline
N = int(input())
LIMIT = N
sequence = list(map(int, input().split()))
# 메모리를 위해 (왼쪽 pal 처리) + (오른쪽 pal 처리) = N 범위만 생성
dp = [[LIMIT] * (N+1-i) for i in range(-1, N)]
# dp[왼쪽 pal 처리][오른쪽 pal 처리]
dp[0][0] = 0
# 왼쪽을 처리하든 오른쪽을 처리하든 r이나 c가 1 증가한다.
# 따라서 r + c = k에서 k를 증가시키면서 처리한다.
for k in range(N):
    for i in range(k+1):
        j = k - i
        # 왼쪽과 오른쪽이 같은 경우 둘 다 pal 처리
        if sequence[i] == sequence[-1-j]:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
        # 다른 경우 숫자를 하나 추가하고, 하나만 pal 처리
        else:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

minimum = LIMIT
for i in range(N+1):
    # r + c = N인 경우
    j = N - i
    minimum = min(minimum, dp[i][j])
    # r + c = N + 1인 경우(길이가 홀수라 중앙에서 왼쪽과 오른쪽에서 둘 다 pal 처리 되는 경우)
    j = N + 1 - i
    minimum = min(minimum, dp[i][j])
print(minimum)
