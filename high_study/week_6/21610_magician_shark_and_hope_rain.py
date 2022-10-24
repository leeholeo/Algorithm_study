# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
# directions = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
# directions = [0] + directions[::-1]
# diag = directions[2:9:2]
# clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
# for _ in range(M):
#     d, s = map(int, input().split())
#     visited = {}
#     for idx, (cr, cc) in enumerate(clouds):
#         ncr = (cr + directions[d][0] * s) % N
#         ncc = (cc + directions[d][1] * s) % N
#         grid[ncr][ncc] += 1
#         visited[(ncr, ncc)] = True
#         clouds[idx] = (ncr, ncc)
#
#     for cr, cc in clouds:
#         for dx, dy in diag:
#             nx, ny = cr+dx, cc+dy
#             if not (0 <= nx < N and 0 <= ny < N):
#                 continue
#
#             if grid[nx][ny]:
#                 grid[cr][cc] += 1
#
#     clouds = []
#     for i in range(N):
#         for j in range(N):
#             if visited.get((i, j), False):
#                 continue
#
#             if grid[i][j] >= 2:
#                 grid[i][j] -= 2
#                 clouds.append((i, j))
#
# total = [sum(grid[i]) for i in range(N)]
# print(sum(total))


# 양승열 - 시간초과.. help..
# 입력부
import sys

n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dia = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
# 스타트 비구름 생성
rain_cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
ans = 0


# 물복사 버그
def water_copy(location):
    # 대각선 4방향 체크 후 값 있는 만큼 cnt++
    for lc in location:
        cnt = 0
        for da in dia:
            nx = lc[0] + da[0]
            ny = lc[1] + da[1]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny] > 0:
                cnt += 1
        A[lc[0]][lc[1]] += cnt


# 비바라기
def rain_thirster(d, s):
    cloud_location = []
    # 비구름 이동
    for rc in rain_cloud:
        rcx = (rc[0] + d[0] * s) % n
        rcy = (rc[1] + d[1] * s) % n
        # 비 내려서 물의 양 1 증가
        A[rcx][rcy] += 1
        # 구름 이동 좌표 저장
        cloud_location.append([rcx, rcy])
    # 구름 사라짐
    rain_cloud.clear()
    # 물복사 버그 시전
    water_copy(cloud_location)
    # 물의 양 >= 2 인 모든칸 구름 생성 및 물의양 -= 2
    for p in range(n):
        for q in range(n):
            if [p, q] not in cloud_location and A[p][q] >= 2:
                A[p][q] -= 2
                rain_cloud.append([p, q])


for i in range(m):
    di, si = map(int, sys.stdin.readline().split())
    di -= 1

    # 비바라기 시전
    rain_thirster(dir[di], si)

# 출력부 - m번 수행 후 바구니 물의 총량
for a in A:
    for b in a:
        ans += b
print(ans)