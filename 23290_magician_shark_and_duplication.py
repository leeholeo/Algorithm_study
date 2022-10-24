def int_1(num_str):
    return int(num_str) - 1


def is_in(r, c):
    if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
        return True
    else:
        return False


def no_shark(r, c):
    if r == sr and c == sc:
        return False
    else:
        return True


def no_smell(r, c):
    if sml_gird[r][c] < 1:
        return True
    else:
        return False


def can_go(nr, nc):
    if is_in(nr, nc) and no_shark(nr, nc) and no_smell(nr, nc):
        return True
    else:
        return False


def fishes_go():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            first_go = 1
            now_fishes = 0
            for d in range(0, -D_LEN, -1):
                now_fishes += dir_grid[r][c][d]
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                if can_go(nr, nc):
                    nxt_cnt_grid[nr][nc] += now_fishes
                    nxt_dir_grid[nr][nc][d] += now_fishes
                    now_fishes = 0
                    if first_go == 1:
                        first_go = d
            if now_fishes != 0:
                if first_go != 1:
                    dr, dc = directions[first_go]
                    nr, nc = r + dr, c + dc
                    nxt_cnt_grid[nr][nc] += now_fishes
                    nxt_dir_grid[nr][nc][d] += now_fishes
                else:
                    for d in range(D_LEN):
                        nxt_cnt_grid[r][c] += dir_grid[r][c][d]
                        nxt_dir_grid[r][c][d] += dir_grid[r][c][d]


# def way_finding(depth, cnt, sr, sc):
#     if depth == 3:
#         return cnt, [(sr, sc)]
#     max_cnt = -1
#     for s in range(S_LEN):
#         dr, dc = s_directions[s]
#         nsr, nsc = sr + dr, sc + dc
#         if not is_in(nsr, nsc):
#             continue
#         ncnt = nxt_cnt_grid[nsr][nsc]
#         nxt_cnt_grid[nsr][nsc] = 0
#         cnt_rtn, way = way_finding(depth+1, cnt+ncnt, nsr, nsc)
#         nxt_cnt_grid[nsr][nsc] = ncnt
#         if cnt_rtn > max_cnt:
#             max_cnt = cnt_rtn
#             max_way = way
#     max_way.append((sr, sc))
#     return max_cnt, max_way

from itertools import product
all_case = list(product(range(4), repeat=3))
def way_finding_2(sr, sc):
    max_cnt = -1
    max_way = ()
    esr, esc = sr, sc
    for case in all_case:
        nsr, nsc = sr, sc
        way = set()
        cnt = 0
        for s in case:
            dr, dc = s_directions[s]
            nsr, nsc = nsr + dr, nsc + dc
            if not is_in(nsr, nsc):
                break
            way.add((nsr, nsc))
        else:
            for wsr, wsc in way:
                cnt += nxt_cnt_grid[wsr][wsc]
            if cnt > max_cnt:
                max_cnt = cnt
                max_way = way
                esr, esc = nsr, nsc
    for wsr, wsc in max_way:
        if nxt_cnt_grid[wsr][wsc] > 0:
            sml_gird[wsr][wsc] = 3
            nxt_dir_grid[wsr][wsc] = [0] * D_LEN
            nxt_cnt_grid[wsr][wsc] = 0
    return esr, esc


def shark_goes(sr, sc):
    # max_cnt, max_way = way_finding(0, 0, sr, sc)
    return way_finding_2(sr, sc)
    # max_way.pop()
    # for nsr, nsc in max_way:
    #     if nxt_cnt_grid[nsr][nsc] > 0:
    #         sml_gird[nsr][nsc] = 3
    #         nxt_dir_grid[nsr][nsc] = [0] * D_LEN
    #         nxt_cnt_grid[nsr][nsc] = 0
    # return max_way[0]


# def remove_sml():
def febreeze():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if sml_gird[r][c] > 0:
                sml_gird[r][c] -= 1


def dup_fishes():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            for d in range(D_LEN):
                nxt_dir_grid[r][c][d] += dir_grid[r][c][d]
            nxt_cnt_grid[r][c] += cnt_grid[r][c]


D_LEN = 8
GRID_SIZE = 4
directions = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
S_LEN = 4
s_directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
M, S = map(int, input().split())
dir_grid = [[[0] * D_LEN for _ in range(GRID_SIZE)] for __ in range(GRID_SIZE)]
nxt_dir_grid = [[[0] * D_LEN for _ in range(GRID_SIZE)] for __ in range(GRID_SIZE)]
cnt_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
nxt_cnt_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
sml_gird = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
for _ in range(M):
    fx, fy, fd = map(int_1, input().split())
    dir_grid[fx][fy][fd] += 1
    cnt_grid[fx][fy] += 1
sr, sc = map(int_1, input().split())

for _ in range(S):
    fishes_go()
    sr, sc = shark_goes(sr, sc)
    febreeze()
    dup_fishes()
    dir_grid = nxt_dir_grid
    cnt_grid = nxt_cnt_grid
    nxt_dir_grid = [[[0] * D_LEN for _ in range(GRID_SIZE)] for __ in range(GRID_SIZE)]
    nxt_cnt_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

print(sum([sum(cnt_grid[i]) for i in range(GRID_SIZE)]))
