directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
N, M = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(N)]
line = []
linearize_drcs = ((0, -1), (1, 0), (0, 1), (-1, 0))
shark_idx = N // 2

# linearize 및 grid에 순서대로 번호 넣기
row = shark_idx
col = shark_idx
drc = 0
cnt = 0
go = 1
for to_go in range(1, N):
    for _ in range(2):
        while to_go >= go:
            dr, dc = linearize_drcs[drc]
            row += dr
            col += dc
            line.append(grids[row][col])
            grids[row][col] = cnt
            cnt += 1
            go += 1
        go = 1
        drc = (drc+1) % 4
line += grids[0][:-1][::-1]
grids[0][:-1] = reversed(list(range(cnt, cnt+N-1)))

# blizzard 피격 linearized idx 기록
linear_idxes = [[None] * shark_idx for _ in range(4)]
for drc in range(4):
    row = shark_idx
    col = shark_idx
    dr, dc = directions[drc]
    go = 0
    while shark_idx > go:
        row += dr
        col += dc
        linear_idxes[drc][go] = grids[row][col]
        go += 1


# 이분탐색으로 0 위치 찾아서 그 이후로 삭제
def cut_zero_tail():
    left = 0
    right = len(line)
    while left < right:
        half = (left + right) // 2
        if line[half] > 0:
            left = half + 1
        else:
            right = half
    return line[:left]


line = cut_zero_tail()

result = 0
# blizzard iteration start
for _ in range(M):
    # blizzard 구슬 제거
    d, s = map(int, input().split())
    d -= 1
    len_of_line = len(line)
    for dist in range(s-1, -1, -1):
        li = linear_idxes[d][dist]
        if li < len_of_line:
            line.pop(li)
        else:
            continue

    # 구슬 변경 먼저 진행
    line.append(10)
    new_line = []
    cnt = 0
    last_marble = line[0]
    for l in line:
        if l == last_marble:
            cnt += 1
        else:
            new_line.append((cnt, last_marble))
            last_marble = l
            cnt = 1
    line = new_line

    # 폭발
    idx = 0
    is_exploded = True
    while is_exploded:
        is_exploded = False
        new_line = []
        last_marble = 10
        idx = 0
        while idx < len(line):
            now_cnt, now_marble = line[idx]
            if now_cnt >= 4:
                is_exploded = True
                result += now_marble * now_cnt
            elif last_marble == now_marble:
                new_line[-1][0] += now_cnt
            else:
                new_line.append([now_cnt, now_marble])
                last_marble = now_marble
            idx += 1
        line = new_line

    # 2중 list를 1중으로 변경
    new_line = []
    for l in line:
        new_line.extend(l)
    line = new_line[:N**2 - 1]

print(result)
