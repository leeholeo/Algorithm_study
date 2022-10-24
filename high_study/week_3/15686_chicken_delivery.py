from itertools import combinations


N, M = map(int, input().split())
field = [input().split() for _ in range(N)]
stores = []
houses = []
for i in range(N):
    for j in range(N):
        if field[i][j] == '2':
            stores.append((i, j))
        elif field[i][j] == '1':
            houses.append((i, j))

mini = 9876543210
for case in combinations(stores, M):
    temp_mini = 0
    for h_row, h_col in houses:
        temp_dist = 100
        for s_row, s_col in case:
            temp_dist = min(temp_dist, abs(h_row-s_row)+abs(h_col-s_col))

        temp_mini += temp_dist

    mini = min(mini, temp_mini)

print(mini)
