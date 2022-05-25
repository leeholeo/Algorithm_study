import sys


def output():
    print(maxi)


def dfs(diag_depth, cnt):
    global maxi
    # 종료조건
    if diag_depth == length:
        maxi = max(maxi, cnt)
        # 최대값이면
        if maxi == length:
            output()
            exit()
    # 왼쪽 상단 좌표
    lefttop_row = max(0, size-1-diag_depth)
    lefttop_col = max(0, diag_depth-size-1)
    # 반대 방향 대각선의 visited배열에서의 시작 좌표
    start_cdiag = abs(size-1-diag_depth)
    # 대각선의 길이
    diag_length = size - start_cdiag
    for k in range(diag_length):
        now_row = lefttop_row + k
        now_col = lefttop_col + k
        # 놓을 수 있다면 놓기
        if chess[now_row][now_col] == '1' and visited[start_cdiag + 2*k] is False:
            visited[start_cdiag + 2*k] = True
            dfs(diag_depth+1, cnt+1)
            visited[start_cdiag + 2*k] = False
        # 안 놓았을 때 가능성이 없다면 prunig
        if length - 1 - diag_depth + cnt > maxi:
            dfs(diag_depth + 1, cnt)


size = int(input())
chess = [sys.stdin.readline().split() for _ in range(size)]
# 반대 대각선의 방문 배열
length = 2*size - 1
visited = [False] * length
maxi = 0
dfs(0, 0)
output()
