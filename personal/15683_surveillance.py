WATCH = 1
UNWATCH = -1

N, M = map(int, input().split())
offices = [list(map(int, input().split())) for _ in range(N)]
CCTVs = []
drc1 = (1, 0)
drc2 = (0, 1)
drc3 = (-1, 0)
drc4 = (0, -1)
CCTVs_drc = [
    [[drc1], [drc2], [drc3], [drc4]],
    [(drc1, drc3), (drc2, drc4)],
    [(drc1, drc2), (drc2, drc3), (drc3, drc4), (drc4, drc1)],
    [(drc1, drc2, drc3), (drc2, drc3, drc4), (drc3, drc4, drc1), (drc4, drc1, drc2)],
    [(drc1, drc2, drc3, drc4)]
]


def watch(r, c, cctv_type, watch=1, cctv_drc=0):
    for dr, dc in CCTVs_drc[cctv_type][cctv_drc]:
        nr, nc = r + dr, c + dc
        while (0 <= nr < N and 0 <= nc < M) and offices[nr][nc] != 'w':
            offices[nr][nc] += watch
            nr += dr
            nc += dc


CCTV_5s = []
for row in range(N):
    for col in range(M):
        if offices[row][col] == 0:
            pass
        elif offices[row][col] == 6:
            offices[row][col] = 'w'
        # 5번 CCTV의 경우 경우의 수가 없으므로 바로 감시
        elif offices[row][col] == 5:
            offices[row][col] = 1
            CCTV_5s.append((row, col))
        else:
            CCTV_type = offices[row][col] - 1
            offices[row][col] = 1
            CCTVs.append((row, col, CCTV_type))

for row, col in CCTV_5s:
    watch(row, col, 4)


def count():
    cnt = 0
    for r in range(N):
        for c in range(M):
            if offices[r][c] == 0:
                cnt += 1
    return cnt


def back_tracking(cctv_num):
    if cctv_num < 0:
        global answer
        answer = min(answer, count())
        return

    r, c, cctv_type = CCTVs[cctv_num]
    for cctv_drc in range(len(CCTVs_drc[cctv_type])):
        watch(r, c, cctv_type, WATCH, cctv_drc)
        back_tracking(cctv_num-1)
        watch(r, c, cctv_type, UNWATCH, cctv_drc)


# 최소 미감시 구역 개수
answer = N * M
back_tracking(len(CCTVs)-1)
print(answer)
