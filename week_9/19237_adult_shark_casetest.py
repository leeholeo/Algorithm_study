f = open('19237_adult_shark_input.txt', 'r')
input = f.readline
for tc in range(100):
    flag = False
    N, M, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sharks = [None] * (M + 1)
    smells = [[] for _ in range(k)]
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                sharks[grid[i][j]] = (i, j)
                smells[k - 1].append((i, j))
                grid[i][j] = str(grid[i][j])
            else:
                grid[i][j] = ''

    sharks_start_drc = list(map(int, input().split()))
    sharks_drc = [None] + [[None] + [list(map(int, input().split())) for __ in range(4)] for _ in range(M)]
    shark_cnt = 1
    for ssd in sharks_start_drc:
        sharks_drc[shark_cnt][0] = ssd
        shark_cnt += 1

    directions = (None, (-1, 0), (1, 0), (0, -1), (0, 1))
    time = 0
    nones = [None] * (M - 1)
    while time <= 1000:
        # 종료 조건
        if sharks[2:] == nones:
            print(time)
            break

        # 한 칸 가기
        for i in range(1, M + 1):
            if tc == 6 and i == 16 and time == 1:
                de = 1
            if sharks[i] is None:
                continue

            r, c = sharks[i]
            visited = 0
            okay = False
            for drc_i in sharks_drc[i][sharks_drc[i][0]]:
                dr, dc = directions[drc_i]
                nr, nc = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                if grid[nr][nc]:
                    if str(i) == grid[nr][nc][0]:
                        if not visited:
                            visited = drc_i
                            okay = True
                    continue

                sharks[i] = (nr, nc)
                sharks_drc[i][0] = drc_i
                okay = True
                break

            else:
                if not okay:
                    if time != 0:
                        de = 1
                    flag = True
                    break
                dr, dc = directions[visited]
                nr, nc = r + dr, c + dc
                sharks[i] = (nr, nc)
                sharks_drc[i][0] = visited

        if flag:
            break
        # 같은 위치 상어 지우기
        temp = {}
        for i in range(1, M + 1):
            if temp.get(sharks[i], 0):
                sharks[i] = None
            else:
                temp[sharks[i]] = i

        # 지난 냄새 격자에서지우기
        for sr, sc in smells[0]:
            grid[sr][sc] = grid[sr][sc][1:]

        # 지난 냄새 지우기
        smells = smells[1:]
        # 현재 냄새 격자에 추가 및 냄새 배열에 추가
        smells.append([])
        for i in range(1, M + 1):
            if sharks[i] is None:
                continue

            r, c = sharks[i]
            grid[r][c] += str(i)
            smells[k - 1].append((r, c))

        # 시간 추가
        time += 1
    else:
        print(-1)

    if flag:
        print('impossible case')

    print(f'tc{tc} is end')

f.close()
