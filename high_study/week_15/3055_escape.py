def bfs():
    # water goes
    global waters_idx
    global Ss_idx
    time = 0
    while Ss_idx:
        time += 1
        temp_waters_idx = []
        while waters_idx:
            r, c = waters_idx.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if forests[nr][nc] == '*':
                    continue
                if forests[nr][nc] == 'X':
                    continue
                if forests[nr][nc] == 'D':
                    continue
                forests[nr][nc] = '*'
                temp_waters_idx.append((nr, nc))
        waters_idx = temp_waters_idx

        # hedgehog goes
        temp_Ss_idx = []
        while Ss_idx:
            r, c = Ss_idx.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if forests[nr][nc] == 'D':
                    return time
                if forests[nr][nc] == '.':
                    forests[nr][nc] = time
                    temp_Ss_idx.append((nr, nc))
        Ss_idx = temp_Ss_idx
    return 'KAKTUS'


R, C = map(int, input().split())
forests = [' '.join(input()).split() for _ in range(R)]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

# input
D_idx = None
Ss_idx = []
waters_idx = []
for row in range(R):
    for col in range(C):
        if forests[row][col] == 'D':
            D_idx = (row, col)
        elif forests[row][col] == 'S':
            Ss_idx.append((row, col))
            forests[row][col] = 0
        elif forests[row][col] == '*':
            waters_idx.append((row, col))

print(bfs())