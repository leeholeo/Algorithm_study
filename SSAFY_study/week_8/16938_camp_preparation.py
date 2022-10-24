'''
N <= 15?
바로 무지성 완전탐색
'''
def problem_selecting(i, summation, low, high):
    # 조건에 안 맞으면 prunning
    if summation > R:
        return
    # N까지 도달했을 때만 경우 체크
    if i >= N:
        # 조건에 안 맞으면 버리기
        if summation < L or high - low < X:
            return
        global answer
        answer += 1
        return
    # 재귀
    problem_selecting(i+1, summation+difficult[i], low, difficult[i])
    problem_selecting(i+1, summation, low, high)


N, L, R, X = map(int, input().split())
difficult = sorted([*map(int, input().split())])
answer = 0
for i in range(1, N+1):
    problem_selecting(i, difficult[i-1], difficult[i-1], difficult[i-1])

print(answer)
