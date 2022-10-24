import sys

'''
솔직히 dfs는 재귀로 대충 짜서 구리다
단순히 두 번 dfs를 돌리는 것과 같으나, 하나의 dfs로 처리하기 위해 conversion을 사용한다.
사방탐색 시, 같은 블럭을 확인할 때 input인 picture에서 현재와 사방이 같은지를 판별하지 않고,
conversion[현재]와 conversion[사방]이 같은지를 판별한다.
parameter: type <- function parameter annotation
'''
def dfs(colors: list(list), conversion: dict(str, int), r: int, c: int) -> bool:
    if colors[r][c] != 0:
        return False
    colors[r][c] = conversion[picture[r][c]]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if colors[r][c] == conversion[picture[nr][nc]]:
            dfs(colors, conversion, nr, nc)
    return True


sys.setrecursionlimit(100000)
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
N = int(input())
picture = [' '.join(input()).split() for _ in range(N)]
normal_conversion = {
    'R': 1,
    'G': 2,
    'B': 3
}
RG_weakness_conversion = {
    'R': 1,
    'G': 1,
    'B': 2
}
normal = [[0] * N for _ in range(N)]
RG_weakness = [[0] * N for _ in range(N)]
normal_cnt = 0
RG_weakness_cnt = 0
for row in range(N):
    for col in range(N):
        if dfs(normal, normal_conversion, row, col):
            normal_cnt += 1
        if dfs(RG_weakness, RG_weakness_conversion, row, col):
            RG_weakness_cnt += 1

print(normal_cnt, RG_weakness_cnt)
