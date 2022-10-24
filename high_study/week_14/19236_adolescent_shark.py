directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
spaces = []
fish_idxes = [None] * 16
for row in range(4):
    fishes = list(map(int, input().split()))
    new_fishes = []
    for col in range(4):
        fish_idx = fishes[2 * col] - 1
        new_fishes.append(fish_idx)
        fish_idxes[fish_idx] = (row, col, fishes[2 * col + 1] - 1)

    spaces.append(new_fishes)

init_fish_idx = spaces[0][0]
init_cnt = init_fish_idx + 1
shark_idx = (0, 0, fish_idxes[init_fish_idx][2])
fish_idxes[init_fish_idx] = None
spaces[0][0] = None
max_cnt = 0


def dfs(cnt):
    global spaces
    global fish_idxes
    global shark_idx
    global max_cnt
    temp_spaces = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            temp_spaces[r][c] = spaces[r][c]

    temp_fish_idxes = fish_idxes[:]

    # fish moves
    for i in range(16):
        if fish_idxes[i] is None:
            continue

        r, c, drc = fish_idxes[i]
        for _ in range(8):
            dr, dc = directions[drc]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 4 and 0 <= nc < 4) or (nr == shark_idx[0] and nc == shark_idx[1]):
                drc = (drc + 1) % 8
                continue

            ni = spaces[nr][nc]
            fish_idxes[i] = (nr, nc, drc)
            if ni is not None:
                fish_idxes[ni] = (r, c, fish_idxes[ni][2])

            spaces[r][c], spaces[nr][nc] = ni, i
            break

    # shark moves
    sr, sc, sdrc = shark_idx
    sdr, sdc = directions[sdrc]
    snr, snc = sr + sdr, sc + sdc
    for __ in range(3):
        if not (0 <= snr < 4 and 0 <= snc < 4):
            break

        if spaces[snr][snc] is not None:
            nfish_idx = spaces[snr][snc]
            shark_idx = fish_idxes[nfish_idx]
            fish_idxes[nfish_idx] = None
            spaces[snr][snc] = None
            dfs(cnt + nfish_idx + 1)
            spaces[snr][snc] = nfish_idx
            fish_idxes[nfish_idx] = shark_idx
            shark_idx = (sr, sc, sdrc)

        snr += sdr
        snc += sdc

    spaces = temp_spaces
    fish_idxes = temp_fish_idxes
    max_cnt = max(max_cnt, cnt)


dfs(init_cnt)
print(max_cnt)
