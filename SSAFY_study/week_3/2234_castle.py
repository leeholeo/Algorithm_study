'''
1. 성의 각 방에 번호를 매긴다(dfs), area_num
    1-1. 번호를 매김과 동시에 크기를 계산한다, area_size
    1-2. 번호를 매김과 동시에 인접한 방으로 의심되는 좌표를 기록해둔다, area_adjacent -> adjacent
2. 각 방마다 인접한 방 후보들의 좌표를 통해 인접한 방들의 넓이 중 최대값을 가져온다, max_adj_size
3. 인접한 방들의 넓이 중 최대 넓이와 해당 방의 넓이를 더해가며 최대 두 개의 방의 넓이 합을 구한다, max_double_size
'''
def sizing(row, col):
    if area_num[row][col]:
        return
    global cnt
    # 방 개수 증가
    cnt += 1
    # 현재 방 번호 지정
    area = cnt
    area_size.append(0)
    area_adjacent = []
    stack = [(row, col)]
    # dfs
    while stack:
        r, c = stack.pop()
        if area_num[r][c]:
            continue
        # 방 크기 기록
        area_size[area] += 1
        # 방 번호 기록
        area_num[r][c] = area
        # 사방탐색
        for i in range(4):
            dr, dc = directions[i]
            nr, nc = r + dr, c + dc
            if not (0 <= nr < M and 0 <= nc < N):
                continue
            # 벽이 있을 때
            if castle[r][c] & (1 << i):
                # 인접 방 후보 좌표 기록
                area_adjacent.append((nr, nc))
            # 벽이 없을 때
            else:
                stack.append((nr, nc))
    adjacent.append(area_adjacent)


directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
N, M = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(M)]
area_num = [[0] * N for _ in range(M)]
area_size = [0]
cnt = 0
adjacent = [[]]
# 방 번호 기록
for i in range(M):
    for j in range(N):
        sizing(i, j)
# 최대 두 개의 방 넓이 합 계산
max_double_size = 0
for i in range(1, cnt+1):
    max_adj_size = 0
    for row, col in adjacent[i]:
        # 인접 방 후보 좌표가 사실은 현재 방과 같은 방일 경우 continue
        if area_num[row][col] != i:
            # 최대 인접 방 넓이
            max_adj_size = max(max_adj_size, area_size[area_num[row][col]])
    # 최대 두 개의 방 넓이 합
    max_double_size = max(max_double_size, max_adj_size + area_size[i])
print(cnt)
print(max(area_size))
print(max_double_size)
