'''
최대를 따지면 ~2M에 가까워서 되려나 했는데 되긴 한다
핵심은 해적 먼저 이동하고 수아가 이동하는 것, 즉 bfs 두 번
모든 칸에 대해 해적이 해당 칸을 최소 몇 번 움직이면 볼 수 있는가(*)를 파악한다
이후 수아는 그 숫자보다 적게 움직이는 경우만 갈 수 있다.
(*)를 판단하는 가장 쉬운 방법은 모든 칸에 대해 몇 번만에 도착하는지를 보고, 모든 칸에 대해
상하좌우로 땅을 만날 때까지 보면서 최솟값을 기록하는 것
하지만 그러면 시간초과(n^4)
따라서 시간을 줄여가면서 최소 몇 번 움직이면 볼 수 있는지를 기록해야 한다.
해당 방법에는 union-find, 모든 행,열에 대해 한번씩 순회하며 기록 등이 있다.
본 코드는 후자이며, 어떤 칸이 속한 행, 열별로 땅을 기준으로 바다를 구획화한다.
즉, r번째 행을 봤을 때, 제일 먼저 있는 바다는 0번, 땅을 한 번 넘어가면 1번 바다...와 같은 식이다.
행, 열 구획별로 최솟값을 기록한다.
그러면 어떤 칸의 (*)는 min(해당 행의 구획의 최솟값, 해당 열의 구획의 최솟값)이다.
이후로는 수아의 bfs를 돌면 끝
'''
from collections import deque
import sys


# 상수
ISLAND = 'I'
SEA = '.'
PIRATE = 'V'
SUA = 'Y'
TREASURE = 'T'
ROW = 0
COL = 1
LIMIT = 98765
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


# input
input = sys.stdin.readline
N, M = map(int, input().split())
t_map = [list(input()) for _ in range(N)]   # 기본적인 지도
area_map = [[[-1, -1] for _ in range(M)] for _ in range(N)] # 해당 칸의 [행 구획, 열 구획]
row_private_arrival = [[] for _ in range(N)]    # [r번째 행 기준][n번째 구획]의 최솟값
col_private_arrival = [[] for _ in range(M)]    # [c번째 열 기준][n번째 구획]의 최솟값
pirate_arrival = [row_private_arrival, col_private_arrival]   # 변수 하나로 사용
pir_r, pir_c = -1, -1
sua_r, sua_c = -1, -1
tre_r, tre_c = -1, -1   # treasure

# 구획 나누기
# row loop
for r in range(N):
    cnt = -1    # 구획 카운트
    last = ISLAND
    for c in range(M):
        if t_map[r][c] != ISLAND:
            if last == ISLAND:
                cnt += 1
            area_map[r][c][ROW] = cnt
            if t_map[r][c] != SEA:
                # 해적, 수아, 보물 위치찾기도 겸
                if t_map[r][c] == PIRATE:
                    pir_r, pir_c = r, c
                elif t_map[r][c] == SUA:
                    sua_r, sua_c = r, c
                elif t_map[r][c] == TREASURE:
                    tre_r, tre_c = r, c
                # 위치 다 찾았으면 그냥 다 바다로 치환
                t_map[r][c] = SEA
        last = t_map[r][c]
    pirate_arrival[ROW][r] = [LIMIT] * (cnt+1)
# col loop
for c in range(M):
    cnt = -1
    last = ISLAND
    for r in range(N):
        if t_map[r][c] == SEA:
            if last == ISLAND:
                cnt += 1
            area_map[r][c][COL] = cnt
        last = t_map[r][c]
    pirate_arrival[COL][c] = [LIMIT] * (cnt+1)

pir_visited = [t_map[r][:] for r in range(N)]
sua_visited = t_map

# 해당 칸을 처음으로 왔는가?
def record(r, c, cnt):
    if pir_visited[r][c] == SEA:
        pir_visited[r][c] = cnt
        row, col = area_map[r][c]
        # 해당 칸의 구획의 최솟값 갱신
        pirate_arrival[ROW][r][row] = min(pirate_arrival[ROW][r][row], cnt)
        pirate_arrival[COL][c][col] = min(pirate_arrival[COL][c][col], cnt)
        return True
    else:
        return False

# 해적 bfs
def bfs_pirate():
    queue = deque()
    record(pir_r, pir_c, 0)
    queue.append((pir_r, pir_c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if record(nr, nc, pir_visited[r][c]+1):
                queue.append((nr, nc))

# 수아가 해당 칸을 갈 수 있는가?
def go(r, c, cnt):
    if r == tre_r and c == tre_c:
        row, col = area_map[r][c]
        if cnt < pirate_arrival[ROW][r][row] and cnt < pirate_arrival[COL][c][col]:
            print("YES")
        else:
            print("NO")
        quit()
    if sua_visited[r][c] == SEA:
        sua_visited[r][c] = cnt
        row, col = area_map[r][c]
        if cnt < pirate_arrival[ROW][r][row] and cnt < pirate_arrival[COL][c][col]:
            return True
    return False

# 수아 bfs
def bfs_sua():
    queue = deque()
    go(sua_r, sua_c, 0)
    queue.append((sua_r, sua_c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if go(nr, nc, sua_visited[r][c]+1):
                queue.append((nr, nc))


bfs_pirate()
bfs_sua()
print("NO")
